
// =======================================================
// LIVE-AKTIVITÄTS-LOGGING & AUDIT-TRAIL
// =======================================================
var acpClientLogs = [];
function acpLog(level, message, details) {
  var now = new Date();
  var timeStr = now.toTimeString().split(' ')[0];
  var entry = {
    time: timeStr,
    level: level || 'info',
    message: message || '',
    details: details || ''
  };
  acpClientLogs.push(entry);

  var consoleEl = document.getElementById("acp-log-console");
  if (consoleEl) {
    if (acpClientLogs.length === 1 && consoleEl.innerText.indexOf("Warte auf Aktionen") !== -1) {
      consoleEl.innerHTML = "";
    }
    var color = '#38bdf8';
    var tag = 'INFO';
    if (level === 'swap') { color = '#facc15'; tag = 'SWAP'; }
    if (level === 'success') { color = '#22c55e'; tag = 'SUCCESS'; }
    if (level === 'error') { color = '#ef4444'; tag = 'ERROR'; }
    if (level === 'server') { color = '#a855f7'; tag = 'SERVER'; }

    var item = document.createElement("div");
    item.style.marginBottom = "6px";
    item.style.wordBreak = "break-all";
    item.innerHTML = '<span style="color:#64748b;">[' + timeStr + ']</span> ' +
      '<span style="color:' + color + '; font-weight:700;">[' + tag + ']</span> ' +
      '<span>' + message + '</span>' +
      (details ? '<div style="color:#94a3b8; font-size:11px; margin-left:14px; margin-top:2px; font-family:monospace;">' + details + '</div>' : '');
    consoleEl.appendChild(item);
    consoleEl.scrollTop = consoleEl.scrollHeight;
  }

  var countBadge = document.getElementById("acp-log-count");
  if (countBadge) {
    countBadge.style.display = "inline-block";
    countBadge.textContent = acpClientLogs.length;
    if (level === 'error') {
      countBadge.style.background = '#ef4444';
    }
  }

  if (level === 'error') {
    console.error('[WebPilot Studio]', timeStr, message, details || '');
  } else {
    console.log('[WebPilot Studio]', timeStr, message, details || '');
  }
}

function acpToggleLogModal() {
  var modal = document.getElementById("acp-log-modal");
  if (!modal) return;
  modal.classList.toggle("is-open");
  acpUpdateBodyModalClass();
}

function acpClearClientLog() {
  acpClientLogs = [];
  var consoleEl = document.getElementById("acp-log-console");
  if (consoleEl) consoleEl.innerHTML = '<div style="color:#64748b; font-style:italic;">Protokoll geleert.</div>';
  var countBadge = document.getElementById("acp-log-count");
  if (countBadge) {
    countBadge.textContent = "0";
    countBadge.style.background = "#d97706";
  }
}

function acpFetchServerLog() {
  var currentJob = getActiveJob();
  var clientSlug = currentJob.folder || 'hiltbrand';
  acpLog('info', '📡 Frage Server-Logbuch ab...', 'Mandant: ' + clientSlug);
  fetch('/api/publish-career/logs?client=' + encodeURIComponent(clientSlug))
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data && data.ok) {
        acpLog('server', '📋 Server-Log geladen (' + data.client + '):', '<pre style="margin:4px 0; white-space:pre-wrap; max-height:200px; overflow-y:auto; background:rgba(0,0,0,0.3); padding:6px; border-radius:4px;">' + (data.log || 'Keine Daten') + '</pre>');
      } else {
        acpLog('error', 'Konnte Server-Log nicht laden: ' + ((data && data.error) || 'Unbekannt'));
      }
    })
    .catch(function(err) {
      acpLog('error', 'Netzwerkfehler beim Laden des Server-Logs: ' + err.message);
    });
}

// =======================================================
// MAGNET-XS COCKPIT FRAMEWORK v3.3.0 (SWISS ARCHITECTURAL CANVAS)
// Build: 2026-10-03 15:30 CEST
// =======================================================
var ACP_COCKPIT_VERSION = "v3.3.0";
var ACP_COCKPIT_BUILD = "2026-10-03 15:30";

function sanitizeStellen(list) {
  if (!Array.isArray(list)) return [];
  return list.filter(function(j) {
    if (!j) return false;
    var f = (j.datei || "").toLowerCase();
    var id = (j.id || "").toLowerCase();
    var t = (j.titel || "").toLowerCase();
    return f.indexOf("cockpit") === -1 && id.indexOf("cockpit") === -1 && t.indexOf("cockpit") === -1;
  });
}

// Mandanten- & Branchen-Profil (Dynamisch injiziert durch build_client_cockpit.py)
var ACP_CLIENT_PROFILE = /* __CLIENT_PROFILE_JSON__ */ || {};

// Manifest-Daten mit robusten Fallbacks
var ACP_BILDER = /* __BILDER_JSON__ */;
var ACP_STELLEN = sanitizeStellen(/* __STELLEN_JSON__ */);

// Globaler State
var activeJobId = "";
var acpMenuOpen = false;
var acpInspectorActive = false;
var acpImagesModalOpen = false;
var acpDirectoryModalOpen = false;
var acpHelpModalOpen = false;
var acpSelectedSwapImage = null; // { rel_path, filename }
var acpTargetSwapSlot = null;    // { slot, isImg, isHero, currentSrc, datei }
var acpCurrentImageFilter = 'alle';
var acpCurrentJobFilter = 'alle';
var acpCurrentImageSort = 'newest';
var acpJustUploadedRelPath = '';
var acpLocalBlobPreviews = {}; // Map: rel_path / filename -> blob: URL (0ms Sofort-Preview aus Browser-RAM)

// Smart Thumbnail Error Handler: Falls Cloudflare Pages Edge das frisch hochgeladene Bild noch deployt (404),
// wird automatisch bis zu 6x alle 2.5s nachgefragt, anstatt sofort permanent 'Bild fehlt' anzuzeigen.
function acpHandleThumbError(imgEl, originalSrc) {
  if (!imgEl) return;
  var retries = parseInt(imgEl.getAttribute("data-acp-retries") || "0", 10);
  if (retries < 6) {
    imgEl.setAttribute("data-acp-retries", (retries + 1).toString());
    imgEl.style.opacity = "0.35";
    imgEl.style.filter = "grayscale(80%)";
    imgEl.style.transition = "opacity 0.3s ease, filter 0.3s ease";
    setTimeout(function() {
      if (!imgEl) return;
      var clean = (originalSrc || imgEl.getAttribute("data-original-src") || imgEl.src || "").split("?")[0];
      if (!clean) return;
      imgEl.src = clean + "?cf_t=" + Date.now();
      imgEl.onload = function() {
        imgEl.style.opacity = "1";
        imgEl.style.filter = "none";
        imgEl.removeAttribute("data-acp-retries");
      };
    }, 2500);
    return;
  }
  // Nach 6 Fehlversuchen (~15s Edge-Deployment Timeout)
  imgEl.style.opacity = "1";
  imgEl.style.filter = "none";
  imgEl.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect fill="%231e293b" width="100" height="100"/><text fill="%2364748b" x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="12">Bild fehlt</text></svg>';
}

// Body Scroll-Lock Manager (Verhindert doppelte Scrollbalken im Vollbildmodus)
function acpUpdateBodyModalClass() {
  var isAnyOpen = false;
  var modals = document.querySelectorAll(".acp-modal-backdrop");
  for (var i = 0; i < modals.length; i++) {
    if (modals[i].classList.contains("is-open")) {
      isAnyOpen = true;
      break;
    }
  }
  if (isAnyOpen) {
    document.body.classList.add("acp-modal-open");
  } else {
    document.body.classList.remove("acp-modal-open");
  }
}

// ESC Taste schliesst Tausch-Modus und alle Modals
document.addEventListener("keydown", function(e) {
  if (e.key === "Escape") {
    if (acpSelectedSwapImage) {
      acpCancelSwap();
      return;
    }
    var sm = document.getElementById("acp-sections-modal");
    if (sm && sm.classList.contains("is-open")) acpToggleSectionsModal();
    var rm = document.getElementById("acp-replace-section-modal");
    if (rm && rm.style.display !== "none") acpCloseReplaceSectionModal();
    var nm = document.getElementById("acp-new-section-modal");
    if (nm && nm.style.display !== "none") acpCloseNewSectionModal();
    var im = document.getElementById("acp-images-modal");
    if (im && im.classList.contains("is-open")) acpToggleImagesModal();
    var dm = document.getElementById("acp-directory-modal");
    if (dm && dm.classList.contains("is-open")) acpToggleDirectoryModal();
    var hm = document.getElementById("acp-help-modal");
    if (hm && hm.classList.contains("is-open")) acpToggleHelpModal();
    var lm = document.getElementById("acp-log-modal");
    if (lm && lm.classList.contains("is-open")) acpToggleLogModal();
  }
});

// -------------------------------------------------------
// [1] STELLEN-VERWALTUNG & JOB PICKER
// -------------------------------------------------------
function getActiveJob() {
  for (var i = 0; i < ACP_STELLEN.length; i++) {
    if (ACP_STELLEN[i].id === activeJobId) return ACP_STELLEN[i];
  }
  return ACP_STELLEN[0] || {};
}

function updateLiveStatusBadge(job) {
  var wrap = document.getElementById("acp-live-badge-wrap");
  if (!wrap) return;
  if (!job) { wrap.innerHTML = ""; return; }
  
  if (job.is_live) {
    var url = job.live_url || "https://dachdecker-berneroberland.ch/jobs/";
    var domain = (job.host_label || "dachdecker-berneroberland.ch");
    wrap.innerHTML = '<a href="' + url + '" target="_blank" class="acp-live-status-pill is-live" title="Diese Stelle ist öffentlich eingebettet. Klicken, um live auf ' + domain + ' anzuschauen!">' +
      '<span class="acp-live-pulse-dot"></span>' +
      '<span>LIVE · ' + domain + '</span>' +
      '<span class="acp-pill-ext">↗</span>' +
    '</a>';
  } else if (job.id && job.id.indexOf("zurbuchen") !== -1) {
    wrap.innerHTML = '<span class="acp-live-status-pill is-ready" title="Bereit zur Einbettung auf zurbuchen-holzbau.ch">' +
      '<span class="acp-draft-dot is-ready"></span>' +
      '<span>BEREIT · Zurbuchen Holzbau</span>' +
    '</span>';
  } else {
    wrap.innerHTML = '<span class="acp-live-status-pill is-draft" title="Sicherer lokaler Entwurf">' +
      '<span class="acp-draft-dot"></span>' +
      '<span>ENTWURF · Vorlage</span>' +
    '</span>';
  }
}

function acpToggleJobDropdown() {
  var dd = document.getElementById("acp-job-dropdown");
  var wrap = document.getElementById("acp-job-picker-wrap");
  if (!dd) return;
  var isOpen = dd.classList.contains("is-open");
  if (isOpen) {
    dd.classList.remove("is-open");
    if (wrap) wrap.classList.remove("is-open");
  } else {
    dd.classList.add("is-open");
    if (wrap) wrap.classList.add("is-open");
  }
}

document.addEventListener("click", function(e) {
  var wrap = document.getElementById("acp-job-picker-wrap");
  if (wrap && !wrap.contains(e.target)) {
    var dd = document.getElementById("acp-job-dropdown");
    if (dd) dd.classList.remove("is-open");
    wrap.classList.remove("is-open");
  }
});

function renderJobPicker() {
  var list = document.getElementById("acp-dropdown-list");
  var countEl = document.getElementById("dropdown-count");
  if (countEl) countEl.textContent = ACP_STELLEN.length;
  if (!list) return;

  var html = "";
  for (var i = 0; i < ACP_STELLEN.length; i++) {
    var j = ACP_STELLEN[i];
    var isActive = (j.id === activeJobId);
    var activeClass = isActive ? "active" : "";
    
    var badgeHtml = "";
    if (j.is_live) {
      badgeHtml = '<span class="acp-badge-mini live">🟢 LIVE</span>';
    } else if (j.id && j.id.indexOf("zurbuchen") !== -1) {
      badgeHtml = '<span class="acp-badge-mini ready">🟡 BEREIT</span>';
    } else {
      badgeHtml = '<span class="acp-badge-mini draft">⚪ ENTWURF</span>';
    }

    html += '<div class="acp-dropdown-item ' + activeClass + '" onclick="acpSwitchJob(\'' + j.id + '\'); acpToggleJobDropdown();">' +
      '<div class="dropdown-item-left">' +
        '<div class="dropdown-item-title">' + (j.icon || "💼") + ' ' + j.titel + '</div>' +
        '<div class="dropdown-item-meta"><span>' + j.firma + '</span> · <span style="color:#38bdf8">' + j.datei + '</span></div>' +
      '</div>' +
      '<div class="dropdown-item-right">' +
        badgeHtml +
        (isActive ? '<span class="check-icon">✓</span>' : '') +
      '</div>' +
    '</div>';
  }
  list.innerHTML = html;

  var currentJob = getActiveJob();
  if (currentJob && currentJob.id) {
    var iconEl = document.getElementById("picker-current-icon");
    var titleEl = document.getElementById("picker-current-title");
    var firmEl = document.getElementById("picker-current-firm");
    if (iconEl) iconEl.textContent = currentJob.icon || "💼";
    if (titleEl) titleEl.textContent = currentJob.titel;
    if (firmEl) firmEl.textContent = currentJob.firma ? currentJob.firma.split(" ")[0] : "";
    updateLiveStatusBadge(currentJob);
  }
}

function acpSwitchJob(jobId, forceReload) {
  activeJobId = jobId;
  var job = getActiveJob();
  if (!job || !job.id) return;
  
  renderJobPicker();

  var hostDomain = job.host_label || "dachdecker-berneroberland.ch";
  var firmaName = job.firma || "Kundenbetrieb";
  var brandColor = job.farb_akzent || "#3b82f6";

  // Studio Device Stage updates
  var stageUrl = document.getElementById("acp-stage-browser-url");
  var stageLink = document.getElementById("acp-stage-external-link");
  var stagePill = document.getElementById("acp-stage-client-pill");
  var subfolder = job.folder || ((job.firma && job.firma.indexOf("Zurbuchen") !== -1) ? "zurbuchen" : "hiltbrand");
  var edgePreviewUrl = job.edge_url || ("https://embed.magnet-xs.ch/" + subfolder + "/" + job.datei);
  var targetLiveUrl = job.live_url || (job.is_live ? ("https://" + hostDomain + "/jobs/") : edgePreviewUrl);

  if (stageUrl) stageUrl.textContent = targetLiveUrl;
  if (stageLink) stageLink.href = targetLiveUrl;
  if (stagePill) stagePill.textContent = firmaName;

  // Fallbacks for mock headers if present
  var hBadge = document.getElementById("host-badge");
  var hTitle = document.getElementById("host-title");
  var hDesc = document.getElementById("host-desc");
  var hHeader = document.getElementById("host-header");
  var fBadge = document.getElementById("host-footer-badge");
  var fTitle = document.getElementById("host-footer-title");
  var fDesc = document.getElementById("host-footer-desc");
  var fFooter = document.getElementById("host-footer");

  if (hBadge) hBadge.innerHTML = '<span>🌐 BEREICH 1: BESTEHENDE WEBSEITE (' + hostDomain + ')</span>';
  if (hTitle) hTitle.textContent = "Kopfzeile der Kunden-Webseite: " + firmaName;
  if (hDesc) hDesc.textContent = "Hier bleibt das Firmenlogo und das normale Navigationsmenü von " + hostDomain + " fix bestehen.";
  if (hHeader) { hHeader.style.borderBottomColor = brandColor; }

  if (fBadge) fBadge.innerHTML = '<span>🌐 BEREICH 3: BESTEHENDE WEBSEITE (' + hostDomain + ')</span>';
  if (fTitle) fTitle.textContent = "Fusszeile der Kunden-Webseite: " + firmaName;
  if (fDesc) fDesc.textContent = "Hier bleibt der bestehende Footer von " + hostDomain + " mit Adressen und Impressum unverändert bestehen.";
  if (fFooter) { fFooter.style.borderTopColor = brandColor; }

  var frame = document.getElementById("acp-widget-viewport");
  if (frame && job.datei) {
    var currentSrc = frame.getAttribute("src") || frame.src || "";
    var cleanCurrent = currentSrc.split("?")[0].replace(/\.html$/, "").split("/").pop().toLowerCase();
    var cleanTarget = job.datei.replace(/\.html$/, "").toLowerCase();
    var isSameJob = (cleanCurrent === cleanTarget);

    if (!isSameJob || forceReload) {
      frame.style.opacity = "0.3";
      var targetSrc = "";
      if (window.location.protocol === "file:") {
        targetSrc = job.datei + "?embed=true";
      } else {
        var base = edgePreviewUrl;
        if (base.indexOf("embed.magnet-xs.ch") !== -1 && base.endsWith(".html")) {
          base = base.replace(/\.html$/, "");
        }
        targetSrc = base + (base.indexOf("?") === -1 ? "?embed=true" : "&embed=true");
      }
      frame.src = targetSrc;
      frame.onload = function() {
        frame.style.opacity = "1";
        if (acpInspectorActive) {
          frame.contentWindow.postMessage({ type: "acp-toggle-inspector", active: true }, "*");
        }
        if (acpSelectedSwapImage) {
          acpDispatchSwapMode(true);
        }
      };
    } else {
      // Job ist bereits aktiv geladen: iFrame NICHT neu laden, damit Bildtausch-Vorschau nicht zurückspringt!
      if (acpInspectorActive && frame.contentWindow) {
        frame.contentWindow.postMessage({ type: "acp-toggle-inspector", active: true }, "*");
      }
      if (acpSelectedSwapImage && frame.contentWindow) {
        acpDispatchSwapMode(true);
      }
    }
  }

  updateSnippetBox();
  acpShowToast("🔄 Vorschau gewechselt auf: <strong>" + job.titel + "</strong>");
}

function updateSnippetBox() {
  var job = getActiveJob();
  if (!job || !job.id) return;
  var label = document.getElementById("code-job-label");
  var pre = document.getElementById("active-widget-snippet");
  if (label) label.textContent = job.titel + " (" + job.firma + ")";
  if (pre) pre.textContent = job.widget_code;
}

function acpCopyActiveCode() {
  var job = getActiveJob();
  if (!job || !job.widget_code) return;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(job.widget_code);
    acpShowToast("📋 <strong>" + job.titel + "</strong> Widget-Code in die Zwischenablage kopiert!");
  } else {
    window.prompt("Kopiere diesen Einbettungs-Code für den Webmaster:", job.widget_code);
  }
}

function acpCopyJobCode(jobId) {
  for (var i = 0; i < ACP_STELLEN.length; i++) {
    if (ACP_STELLEN[i].id === jobId) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(ACP_STELLEN[i].widget_code);
        acpShowToast("📋 Widget-Code für <strong>" + ACP_STELLEN[i].titel + "</strong> kopiert!");
      } else {
        window.prompt("Kopiere diesen Einbettungs-Code:", ACP_STELLEN[i].widget_code);
      }
      return;
    }
  }
}

function acpCopyAiPrompt(btn) {
  var text = "Bitte gib mir den Quellcode immer als eine einzige, vollständige und ungekürzte HTML-Datei aus – ausnahmslos von <!DOCTYPE html> bis </html>. Verwende keine Code-Auslassungen (wie // ... restlicher Code ...), keine Zusammenfassungen und erstelle die Ausgabe direkt als einhängenden Code-Block in deiner Antwort.";
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text);
    acpShowToast("📋 KI-Befehl in die Zwischenablage kopiert!");
    if (btn) {
      var orig = btn.textContent;
      btn.textContent = "✓ Kopiert!";
      setTimeout(function() { btn.textContent = orig; }, 2000);
    }
  } else {
    window.prompt("Kopiere diesen Befehl für deine KI:", text);
  }
}

function acpCopyOnlineUrl(btn) {
  var url = "https://embed.magnet-xs.ch/hiltbrand/cockpit";
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(url);
    acpShowToast("📋 <strong>Online-Cockpit Link kopiert!</strong><br><small>" + url + "</small>");
    if (btn) {
      var orig = btn.textContent;
      btn.textContent = "✓ Kopiert!";
      setTimeout(function() { btn.textContent = orig; }, 2000);
    }
  } else {
    window.prompt("Kopiere die Online-Cockpit Adresse:", url);
  }
}

function acpToggleHelpModal() {
  var modal = document.getElementById("acp-help-modal");
  if (!modal) return;
  modal.classList.toggle("is-open");
  acpUpdateBodyModalClass();
}

// -------------------------------------------------------
// [2] BILDER-VERZEICHNIS & ASSET-GALERIE
// -------------------------------------------------------
function acpToggleImagesModal() {
  acpImagesModalOpen = !acpImagesModalOpen;
  var modal = document.getElementById("acp-images-modal");
  if (modal) modal.classList.toggle("is-open", acpImagesModalOpen);
  acpUpdateBodyModalClass();
  
  // Spinner sicherheitshalber deaktivieren
  var statusBox = document.getElementById("acp-upload-status");
  if (statusBox) statusBox.classList.remove("is-active");

  if (acpImagesModalOpen) {
    acpRefreshImages();
    acpRenderImagesGrid();
  }
}

function acpSetImageFilter(category) {
  acpCurrentImageFilter = category;
  var pills = document.querySelectorAll(".acp-filter-pill");
  pills.forEach(function(p) { p.classList.remove("active"); });
  if (event && event.target) event.target.classList.add("active");
  acpRenderImagesGrid();
}

function acpFilterImages() {
  acpRenderImagesGrid();
}

function acpSetImageSort(sortKey) {
  acpCurrentImageSort = sortKey;
  acpRenderImagesGrid();
}

function acpRenderImagesGrid() {
  var grid = document.getElementById("acp-images-grid");
  if (!grid) return;

  var searchInput = document.getElementById("acp-images-search");
  var query = (searchInput ? searchInput.value : "").toLowerCase().trim();

  var countAll = ACP_BILDER.length;
  var countUsed = ACP_BILDER.filter(function(b) { return b.is_used; }).length;
  var elAll = document.getElementById("count-all");
  var elUsed = document.getElementById("count-used");
  if (elAll) elAll.textContent = countAll;
  if (elUsed) elUsed.textContent = countUsed;

  var filtered = ACP_BILDER.filter(function(b) {
    if (acpCurrentImageFilter === 'used' && !b.is_used) return false;
    if (acpCurrentImageFilter === 'hero' && b.category !== 'Hero & Header') return false;
    if (acpCurrentImageFilter === 'team' && b.category !== 'Team & Porträt') return false;
    if (acpCurrentImageFilter === 'benefit') {
      var workLabel = (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.work_category_label) || 'Baustelle & Benefit';
      if (b.category !== 'Baustelle & Benefit' && b.category !== 'Baustelle & Projekte' && b.category !== workLabel) return false;
    }
    if (acpCurrentImageFilter === 'logo' && b.category !== 'Logo & Icon') return false;

    if (query) {
      var matchName = b.filename.toLowerCase().indexOf(query) !== -1;
      var matchPath = b.rel_path.toLowerCase().indexOf(query) !== -1;
      var matchCat = (b.category || '').toLowerCase().indexOf(query) !== -1;
      return matchName || matchPath || matchCat;
    }
    return true;
  });

  // Sortierung anwenden
  filtered.sort(function(a, b) {
    if (acpCurrentImageSort === 'newest') {
      return (b.mtime || 0) - (a.mtime || 0);
    }
    if (acpCurrentImageSort === 'oldest') {
      return (a.mtime || 0) - (b.mtime || 0);
    }
    if (acpCurrentImageSort === 'name_asc') {
      return (a.filename || '').localeCompare(b.filename || '');
    }
    if (acpCurrentImageSort === 'name_desc') {
      return (b.filename || '').localeCompare(a.filename || '');
    }
    if (acpCurrentImageSort === 'size_desc') {
      return (b.size_kb || 0) - (a.size_kb || 0);
    }
    if (acpCurrentImageSort === 'used') {
      if (a.is_used !== b.is_used) {
        return a.is_used ? -1 : 1;
      }
      return (b.mtime || 0) - (a.mtime || 0);
    }
    return 0;
  });

  if (filtered.length === 0) {
    grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; color: #94a3b8;">' +
      '<div style="font-size: 32px; margin-bottom: 10px;">🔍</div>' +
      '<div>Keine Bilder für diese Auswahl gefunden.</div>' +
    '</div>';
    return;
  }

  var html = '';
  for (var i = 0; i < filtered.length; i++) {
    var img = filtered[i];
    var isNewlyUploaded = acpJustUploadedRelPath && (img.rel_path === acpJustUploadedRelPath || img.filename === acpJustUploadedRelPath);
    var cardClasses = 'acp-image-card' + (isNewlyUploaded ? ' is-just-uploaded' : '');
    var newBadge = isNewlyUploaded ? '<div class="acp-card-new-badge">✨ NEU HOCHGELADEN</div>' : '';
    var dateMeta = img.mtime_str ? ' · ' + img.mtime_str : '';
    var badgeClass = img.is_used ? 'badge-used' : 'badge-free';
    var badgeText = img.is_used ? '🟢 Im Einsatz (' + img.used_in.length + ')' : '⚪ Frei verfügbar';
    var usedDetails = '';
    if (img.is_used && img.used_in && img.used_in.length > 0) {
      usedDetails = '<div style="font-size:10px; color:#94a3b8; margin-top:3px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;" title="' + img.used_in.map(function(u){return u.datei;}).join(', ') + '">' +
        img.used_in.map(function(u){ return u.datei; }).join(', ') +
      '</div>';
    }

    var effectiveThumbSrc = acpLocalBlobPreviews[img.rel_path] || acpLocalBlobPreviews[img.filename] || img.rel_path;

    html += '<div class="' + cardClasses + '">' +
      '<div class="acp-card-thumb-wrap">' +
        newBadge +
        '<img src="' + effectiveThumbSrc + '" alt="' + img.filename + '" class="acp-card-thumb" loading="lazy" data-original-src="' + img.rel_path + '" onerror="acpHandleThumbError(this, \'' + img.rel_path.replace(/'/g, "\\'") + '\');">' +
      '</div>' +
      '<div class="acp-card-body">' +
        '<div class="acp-card-title" title="' + img.filename + '">' + img.filename + '</div>' +
        '<div class="acp-card-meta">' + img.dimensions + ' · ' + img.size_kb + ' KB' + dateMeta + '</div>' +
        '<div class="acp-card-badge ' + badgeClass + '">' + badgeText + usedDetails + '</div>' +
        '<div class="acp-card-actions">' +
          '<button type="button" class="btn-card-swap" onclick="acpSelectSwapImage(\'' + img.rel_path + '\', \'' + img.filename + '\')" title="Als neues Foto für Bildtausch auswählen">🎯 Als Tausch-Bild wählen</button>' +
          '<button type="button" class="btn-card-copy" onclick="acpCopyImagePath(\'' + img.rel_path + '\')" title="Pfad in die Zwischenablage kopieren">📋 Pfad</button>' +
          '<button type="button" class="btn-card-delete ' + (img.is_used ? 'is-disabled' : '') + '" onclick="acpDeleteImage(\'' + img.rel_path + '\', \'' + img.filename.replace(/'/g, "\\'") + '\', ' + (img.is_used ? 'true' : 'false') + ')" title="' + (img.is_used ? 'Im Einsatz — kann nicht gelöscht werden' : 'Foto aus Pool & Cloudflare löschen') + '">🗑️</button>' +
        '</div>' +
      '</div>' +
    '</div>';
  }
  grid.innerHTML = html;
}

function acpCopyImagePath(relPath) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(relPath);
  }
  acpShowToast('📋 Bildpfad <code>' + relPath + '</code> kopiert!');
}

function acpRefreshImages(highlightRelPath, showToast) {
  if (window.location.protocol === "http:" || window.location.protocol === "https:") {
    fetch("bilder.json?t=" + Date.now())
      .then(function(res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function(data) {
        if (Array.isArray(data) && data.length > 0) {
          ACP_BILDER = data;
          if (highlightRelPath) {
            var foundIdx = -1;
            for (var i = 0; i < ACP_BILDER.length; i++) {
              if (ACP_BILDER[i].rel_path === highlightRelPath || ACP_BILDER[i].filename === highlightRelPath) {
                foundIdx = i;
                break;
              }
            }
            if (foundIdx > -1) {
              var item = ACP_BILDER.splice(foundIdx, 1)[0];
              ACP_BILDER.unshift(item);
            }
          }
          acpRenderImagesGrid();
          if (showToast) {
            acpShowToast('🔄 Bilder-Pool aktualisiert (' + ACP_BILDER.length + ' Fotos bereit)');
          }
        }
      })
      .catch(function(err) {
        console.warn("Konnte bilder.json nicht dynamisch abrufen:", err.message);
      });
  }
}

function acpHandleFileInput(event) {
  if (!event || !event.target || !event.target.files) return;
  var file = event.target.files[0];
  if (file) {
    acpUploadImageFile(file);
  }
  event.target.value = "";
}

function acpInitUploadDropzone() {
  var zone = document.getElementById("acp-upload-zone");
  if (!zone) return;

  ["dragenter", "dragover"].forEach(function(eventName) {
    zone.addEventListener(eventName, function(e) {
      e.preventDefault();
      e.stopPropagation();
      zone.classList.add("dragover");
    }, false);
  });

  ["dragleave", "drop"].forEach(function(eventName) {
    zone.addEventListener(eventName, function(e) {
      e.preventDefault();
      e.stopPropagation();
      zone.classList.remove("dragover");
    }, false);
  });

  zone.addEventListener("drop", function(e) {
    var dt = e.dataTransfer;
    if (dt && dt.files && dt.files.length > 0) {
      acpUploadImageFile(dt.files[0]);
    }
  }, false);
}

function acpUploadImageFile(file) {
  if (!file) return;

  if (window.location.protocol === "file:") {
    acpShowToast("📁 Im lokalen Dateimodus: Bitte lege Fotos direkt in deinen Ordner <code>images/</code> ab.");
    return;
  }

  var validExts = [".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif"];
  var fileName = file.name.toLowerCase();
  var isValidExt = validExts.some(function(ext) { return fileName.endsWith(ext); });
  if (!isValidExt) {
    acpShowToast("⚠️ Dateiformat wird nicht unterstützt. Erlaubt sind JPG, PNG, WebP, SVG, GIF.");
    return;
  }

  if (file.size > 15 * 1024 * 1024) {
    acpShowToast("⚠️ Das Foto ist grösser als 15 MB. Bitte wähle eine kleinere Datei.");
    return;
  }

  var statusBox = document.getElementById("acp-upload-status");
  var statusText = document.getElementById("acp-upload-status-text");
  if (statusBox) statusBox.classList.add("is-active");
  if (statusText) statusText.textContent = "Foto '" + file.name + "' wird hochgeladen & bereitgestellt...";

  // 0ms Sofort-Vorschau: Erstelle lokalen Blob-URL direkt aus dem File-Objekt im Browser-RAM
  var localBlobUrl = "";
  try {
    if (window.URL && window.URL.createObjectURL) {
      localBlobUrl = URL.createObjectURL(file);
      acpLocalBlobPreviews[file.name] = localBlobUrl;
      acpLocalBlobPreviews["images/" + file.name] = localBlobUrl;
      var safeName = file.name.replace(/[^a-zA-Z0-9._-]/g, "_");
      acpLocalBlobPreviews[safeName] = localBlobUrl;
      acpLocalBlobPreviews["images/" + safeName] = localBlobUrl;
    }
  } catch (blobErr) {
    console.warn("Konnte Blob-Preview nicht erstellen:", blobErr);
  }

  var fd = new FormData();
  fd.append("file", file);

  fetch("/api/publish-career/upload-image", {
    method: "POST",
    body: fd
  })
    .then(function(res) {
      return res.json().then(function(json) {
        if (!res.ok) throw new Error(json.error || ("HTTP " + res.status));
        return json;
      });
    })
    .then(function(data) {
      if (statusBox) statusBox.classList.remove("is-active");
      if (data.ok) {
        if (localBlobUrl) {
          if (data.rel_path) acpLocalBlobPreviews[data.rel_path] = localBlobUrl;
          if (data.filename) acpLocalBlobPreviews[data.filename] = localBlobUrl;
        }
        if (Array.isArray(data.bilder) && data.bilder.length > 0) {
          ACP_BILDER = data.bilder;
        }
        acpJustUploadedRelPath = data.rel_path;
        acpCurrentImageSort = "newest";
        var sortEl = document.getElementById("acp-images-sort");
        if (sortEl) sortEl.value = "newest";

        acpRenderImagesGrid();

        // Automatisch nach oben scrollen, damit das neue Bild sofort im Blickfeld ist
        var modal = document.getElementById("acp-images-modal");
        if (modal) {
          var modalBody = modal.querySelector(".acp-modal-body");
          if (modalBody) modalBody.scrollTop = 0;
        }

        acpShowToast("✅ Foto <code>" + data.filename + "</code> (" + data.size_kb + " KB) erfolgreich im Bilder-Pool bereitgestellt!");
      } else {
        throw new Error(data.error || "Upload fehlgeschlagen");
      }
    })
    .catch(function(err) {
      if (statusBox) statusBox.classList.remove("is-active");
      console.error("Upload-Fehler:", err);
      acpShowToast("🚨 Upload fehlgeschlagen: " + err.message);
      acpReportClientEvent("error", "Foto-Upload im Cockpit fehlgeschlagen", err.message);
    });
}

function acpDeleteImage(relPath, filename, isUsed) {
  if (isUsed) {
    acpShowToast("⚠️ Das Foto <code>" + filename + "</code> wird aktuell in einer Stelle verwendet und kann nicht gelöscht werden. Tausche es zuerst aus.");
    return;
  }

  if (window.location.protocol === "file:") {
    acpShowToast("📁 Im lokalen Dateimodus: Bitte lösche die Datei direkt aus deinem Ordner <code>images/</code>.");
    return;
  }

  var confirmed = confirm("Möchtest du das Foto '" + filename + "' wirklich löschen?\n\nEs wird dauerhaft aus dem Bilder-Pool, dem lokalen Ordner und von Cloudflare Pages entfernt.");
  if (!confirmed) return;

  var statusBox = document.getElementById("acp-upload-status");
  var statusText = document.getElementById("acp-upload-status-text");
  if (statusBox) statusBox.classList.add("is-active");
  if (statusText) statusText.textContent = "Foto '" + filename + "' wird gelöscht...";

  fetch("/api/publish-career/delete-image", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ rel_path: relPath })
  })
    .then(function(res) {
      return res.json().then(function(json) {
        if (!res.ok) throw new Error(json.error || ("HTTP " + res.status));
        return json;
      });
    })
    .then(function(data) {
      if (statusBox) statusBox.classList.remove("is-active");
      if (data.ok) {
        if (Array.isArray(data.bilder)) {
          ACP_BILDER = data.bilder;
        } else {
          ACP_BILDER = ACP_BILDER.filter(function(b) { return b.rel_path !== relPath; });
        }
        if (acpJustUploadedRelPath === relPath) {
          acpJustUploadedRelPath = null;
        }
        delete acpLocalBlobPreviews[relPath];
        delete acpLocalBlobPreviews[filename];
        acpRenderImagesGrid();
        acpShowToast("🗑️ Foto <code>" + filename + "</code> erfolgreich gelöscht.");
      } else {
        throw new Error(data.error || "Löschen fehlgeschlagen");
      }
    })
    .catch(function(err) {
      if (statusBox) statusBox.classList.remove("is-active");
      console.error("Lösch-Fehler:", err);
      acpShowToast("🚨 Löschen fehlgeschlagen: " + err.message);
      acpReportClientEvent("error", "Foto-Löschen im Cockpit fehlgeschlagen", err.message);
    });
}

function acpEnsureSpotlightCssInDoc(doc) {
  if (!doc) return;
  var existing = doc.getElementById("acp-swap-spotlight-css");
  if (!existing) {
    var style = doc.createElement("style");
    style.id = "acp-swap-spotlight-css";
    style.textContent = [
      "body.acp-swap-mode-active .top-bar,",
      "body.acp-swap-mode-active header:not(:has(img)),",
      "body.acp-swap-mode-active h1,",
      "body.acp-swap-mode-active h2,",
      "body.acp-swap-mode-active h3,",
      "body.acp-swap-mode-active h4,",
      "body.acp-swap-mode-active h5,",
      "body.acp-swap-mode-active p,",
      "body.acp-swap-mode-active .eyebrow,",
      "body.acp-swap-mode-active .eyebrow2,",
      "body.acp-swap-mode-active .trust,",
      "body.acp-swap-mode-active .hero-cta,",
      "body.acp-swap-mode-active .btn,",
      "body.acp-swap-mode-active button,",
      "body.acp-swap-mode-active .gruende,",
      "body.acp-swap-mode-active .grund,",
      "body.acp-swap-mode-active .inserat,",
      "body.acp-swap-mode-active .inserat-bg,",
      "body.acp-swap-mode-active .blitz-bewerbung,",
      "body.acp-swap-mode-active .blitz-karte,",
      "body.acp-swap-mode-active .form-box,",
      "body.acp-swap-mode-active form,",
      "body.acp-swap-mode-active .faq,",
      "body.acp-swap-mode-active .rot-linie,",
      "body.acp-swap-mode-active .sticky-cta,",
      "body.acp-swap-mode-active .wa-direkt-box,",
      "body.acp-swap-mode-active .kontakt-karte,",
      "body.acp-swap-mode-active .vorteil,",
      "body.acp-swap-mode-active .fakten,",
      "body.acp-swap-mode-active .leistungen,",
      "body.acp-swap-mode-active .cta-band,",
      "body.acp-swap-mode-active footer {",
      "  opacity: 0.25 !important;",
      "  pointer-events: none !important;",
      "  transition: opacity 0.3s ease !important;",
      "}",
      "body.acp-swap-mode-active .hero {",
      "  position: relative !important;",
      "  cursor: pointer !important;",
      "  pointer-events: auto !important;",
      "  outline: 5px solid #facc15 !important;",
      "  outline-offset: -5px !important;",
      "  box-shadow: inset 0 0 100px rgba(250, 204, 21, 0.45), 0 0 60px rgba(250, 204, 21, 0.7) !important;",
      "  opacity: 1 !important;",
      "}",
      "body.acp-swap-mode-active .hero:hover {",
      "  outline-color: #ffffff !important;",
      "  box-shadow: inset 0 0 120px rgba(250, 204, 21, 0.65), 0 0 80px rgba(250, 204, 21, 0.9) !important;",
      "}",
      "body.acp-swap-mode-active .hero::before {",
      "  content: \"⚡ HIER KLICKEN: HERO-BILD SOFORT ERSETZEN (oder ESC zum Abbrechen)\" !important;",
      "  position: absolute !important;",
      "  top: 24px !important;",
      "  left: 50% !important;",
      "  transform: translateX(-50%) !important;",
      "  z-index: 1000 !important;",
      "  background: #facc15 !important;",
      "  color: #0f172a !important;",
      "  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;",
      "  font-size: 14px !important;",
      "  font-weight: 800 !important;",
      "  letter-spacing: 0.5px !important;",
      "  padding: 10px 24px !important;",
      "  border-radius: 9999px !important;",
      "  box-shadow: 0 4px 25px rgba(0,0,0,0.7), 0 0 30px rgba(250, 204, 21, 0.9) !important;",
      "  pointer-events: none !important;",
      "  animation: acpPulseBadge 1.8s infinite ease-in-out !important;",
      "  white-space: nowrap !important;",
      "}",
      "body.acp-swap-mode-active img,",
      "body.acp-swap-mode-active [data-slot*=\"bild\"],",
      "body.acp-swap-mode-active [data-slot*=\"foto\"],",
      "body.acp-swap-mode-active [data-slot*=\"image\"],",
      "body.acp-swap-mode-active [data-slot*=\"logo\"],",
      "body.acp-swap-mode-active .kollege img,",
      "body.acp-swap-mode-active .team-card img {",
      "  opacity: 1 !important;",
      "  outline: 4px solid #facc15 !important;",
      "  outline-offset: 4px !important;",
      "  box-shadow: 0 0 35px rgba(250, 204, 21, 0.95), 0 0 15px rgba(250, 204, 21, 0.8) !important;",
      "  cursor: pointer !important;",
      "  pointer-events: auto !important;",
      "  position: relative !important;",
      "  z-index: 200 !important;",
      "  transition: transform 0.2s ease, box-shadow 0.2s ease, outline-color 0.2s ease !important;",
      "}",
      "body.acp-swap-mode-active img:hover,",
      "body.acp-swap-mode-active [data-slot*=\"bild\"]:hover,",
      "body.acp-swap-mode-active [data-slot*=\"foto\"]:hover {",
      "  transform: scale(1.06) !important;",
      "  outline-color: #ffffff !important;",
      "  box-shadow: 0 0 50px rgba(250, 204, 21, 1), 0 0 25px #ffffff !important;",
      "}",
      "body.acp-swap-mode-active .team,",
      "body.acp-swap-mode-active .kollegen,",
      "body.acp-swap-mode-active .kollege {",
      "  opacity: 1 !important;",
      "  pointer-events: auto !important;",
      "}",
      "body.acp-swap-mode-active .kollege strong,",
      "body.acp-swap-mode-active .kollege span {",
      "  opacity: 0.9 !important;",
      "  color: #facc15 !important;",
      "}"
    ].join("\n");
    doc.head.appendChild(style);
  }
}

function acpDispatchSwapMode(active) {
  var frame = document.getElementById("acp-widget-viewport");
  if (frame && frame.contentWindow) {
    frame.contentWindow.postMessage({ type: "acp-toggle-swap-mode", active: !!active }, "*");
    try {
      if (frame.contentDocument && frame.contentDocument.body) {
        frame.contentDocument.body.classList.toggle("acp-swap-mode-active", !!active);
        acpEnsureSpotlightCssInDoc(frame.contentDocument);
      }
    } catch(e) {}
  }
}

function getUsedImagesForCurrentJob() {
  var currentJob = getActiveJob();
  var activeFile = currentJob.datei || 'Hiltbrand_Dachdecker_Pragmatisch.html';
  var list = [];
  var seen = {};
  if (Array.isArray(ACP_BILDER)) {
    for (var i = 0; i < ACP_BILDER.length; i++) {
      var b = ACP_BILDER[i];
      if (b.is_used && Array.isArray(b.used_in)) {
        for (var k = 0; k < b.used_in.length; k++) {
          if (b.used_in[k].datei === activeFile) {
            var key = b.filename;
            if (!seen[key]) {
              seen[key] = true;
              list.push({
                filename: b.filename,
                rel_path: b.rel_path,
                slot: b.used_in[k].slot || (b.used_in[k].is_hero ? 'hero.hintergrund.bild' : b.filename),
                is_hero: !!b.used_in[k].is_hero,
                category: b.category || ''
              });
            }
            break;
          }
        }
      }
    }
  }
  return list;
}

function acpSelectSwapImage(relPath, filename) {
  acpSelectedSwapImage = { rel_path: relPath, filename: filename };
  acpLog("info", "📷 Tausch-Bild ausgewählt: " + filename, "Pfad: " + relPath);
  if (acpImagesModalOpen) {
    acpToggleImagesModal();
  }

  var dock = document.getElementById("acp-swap-dock");
  var thumb = document.getElementById("acp-swap-source-thumb");
  var nameEl = document.getElementById("acp-swap-source-name");
  var targetHint = document.getElementById("acp-swap-target-hint");
  var actionsBox = document.getElementById("acp-swap-actions");

  var effectiveThumb = acpLocalBlobPreviews[relPath] || acpLocalBlobPreviews[filename] || relPath;
  if (thumb) {
    thumb.src = effectiveThumb;
    thumb.onerror = function() {
      acpHandleThumbError(thumb, relPath);
    };
  }
  if (nameEl) nameEl.textContent = filename;

  var usedImages = getUsedImagesForCurrentJob();

  if (targetHint) {
    if (usedImages.length > 0) {
      var btnsHtml = '<div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">' +
        '<span style="color:#facc15; font-size:12px; font-weight:700;">👉 Wähle das zu ersetzende Bild:</span>';
      for (var u = 0; u < usedImages.length; u++) {
        var uImg = usedImages[u];
        var label = uImg.is_hero ? ('🖼️ Hero-Hintergrund (' + uImg.filename + ')') : ('📷 ' + uImg.filename);
        btnsHtml += '<button type="button" class="btn-swap-target-choice" onclick="acpSelectTargetDirect(\'' + uImg.rel_path + '\', \'' + uImg.slot + '\', ' + uImg.is_hero + ')">' + label + '</button>';
      }
      btnsHtml += '<span style="color:#94a3b8; font-size:11px;">(oder klicke in der Vorschau darauf)</span></div>';
      targetHint.innerHTML = btnsHtml;
    } else {
      targetHint.innerHTML = '<span style="color:#facc15; font-size:12px; font-weight:700;">👉 Klicke jetzt in der Vorschau auf das Bild, das du ersetzen möchtest...</span>';
    }
  }

  if (actionsBox) actionsBox.style.display = "none";
  if (dock) {
    dock.classList.add("is-visible");
    dock.classList.add("is-active");
  }

  if (!acpInspectorActive) {
    acpToggleInspector();
  }

  acpDispatchSwapMode(true);

  window.scrollTo({ top: 0, behavior: "smooth" });
  acpShowToast('🎯 Tausch-Bild gewählt: <strong>' + filename + '</strong><br><small>Wähle nun das Zielbild in der gelben Leiste oben oder klicke in der Vorschau darauf.</small>', 5000);
}

function acpSelectTargetDirect(srcPath, slotName, isHero) {
  acpHandleSlotClick({
    slot: slotName,
    isImg: true,
    isHero: isHero,
    currentSrc: srcPath
  });
}

function acpResetTargetChoice() {
  acpTargetSwapSlot = null;
  var actionsBox = document.getElementById("acp-swap-actions");
  if (actionsBox) actionsBox.style.display = "none";
  if (acpSelectedSwapImage) {
    acpSelectSwapImage(acpSelectedSwapImage.rel_path, acpSelectedSwapImage.filename);
  }
}

function acpCancelSwap(silent) {
  acpSelectedSwapImage = null;
  acpTargetSwapSlot = null;
  var dock = document.getElementById("acp-swap-dock");
  if (dock) {
    dock.classList.remove("is-visible");
    dock.classList.remove("is-active");
  }
  var targetHint = document.getElementById("acp-swap-target-hint");
  if (targetHint) {
    targetHint.textContent = "👉 Klicke jetzt in der Vorschau auf das zu ersetzende Bild!";
    targetHint.style.color = "#94a3b8";
  }
  var actionsBox = document.getElementById("acp-swap-actions");
  if (actionsBox) actionsBox.style.display = "none";
  acpDispatchSwapMode(false);
  if (!silent) {
    acpShowToast('Tausch-Vorgang beendet.');
  }
}

function acpHandleSlotClick(data) {
  if (!acpSelectedSwapImage) {
    acpShowToast('💡 <strong>Klick-Inspektor:</strong> Öffne zuerst oben <strong>[ 🖼️ Bilder ]</strong> und wähle ein Tausch-Foto aus!', 4000);
    return;
  }

  var currentJob = getActiveJob();
  var activeFile = currentJob.datei || 'Hiltbrand_Dachdecker_Pragmatisch.html';

  var currentSrc = (data.currentSrc || data.src || '').replace(/['"]/g, '').split('?')[0].trim();
  if (!currentSrc && data.isHero) {
    currentSrc = 'images/hero.jpg';
  }

  acpTargetSwapSlot = {
    slot: data.slot || 'hero.hintergrund.bild',
    isImg: data.isImg,
    isHero: data.isHero,
    currentSrc: currentSrc,
    datei: activeFile
  };

  // 1. Sofortige visuelle Rückmeldung im iframe (Zero-Latency Feedback!)
  var frame = document.getElementById("acp-widget-viewport");
  if (frame && frame.contentWindow) {
    var effectivePreviewSrc = acpLocalBlobPreviews[acpSelectedSwapImage.rel_path] || acpLocalBlobPreviews[acpSelectedSwapImage.filename] || acpSelectedSwapImage.rel_path;
    frame.contentWindow.postMessage({
      type: "acp-apply-swap-preview",
      slot: acpTargetSwapSlot.slot,
      isHero: acpTargetSwapSlot.isHero,
      newSrc: effectivePreviewSrc,
      oldSrc: acpTargetSwapSlot.currentSrc
    }, "*");
  }

  var targetHint = document.getElementById("acp-swap-target-hint");
  var actionsBox = document.getElementById("acp-swap-actions");
  var cleanOld = acpTargetSwapSlot.currentSrc.split('/').pop() || acpTargetSwapSlot.slot;
  var cleanNew = acpSelectedSwapImage.filename;
  acpLog("swap", "🎯 Tauschziel im Inserat gewählt: " + cleanOld + " ➔ " + cleanNew, "Datei: " + activeFile + " · Slot: " + acpTargetSwapSlot.slot);

  if (targetHint) {
    targetHint.innerHTML = '<span style="color:#22c55e; font-weight:700;">✅ Tausche:</span> ' +
      '<strong style="color:#f87171;">' + cleanOld + '</strong> ➔ <strong style="color:#38bdf8;">' + cleanNew + '</strong> in <code>' + activeFile + '</code>';
  }
  if (actionsBox) {
    actionsBox.style.display = "flex";
  }

  // 2. Automatischer 1-Klick-Tausch sofort ausführen!
  acpExecuteDirectSwap();
}

function acpReportClientEvent(level, message, details) {
  try {
    if (window.location.protocol === "http:" || window.location.protocol === "https:") {
      fetch("/api/publish-career/log-client-event", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          level: level || "info",
          message: message || "Browser-Ereignis",
          details: details ? (typeof details === "string" ? details : JSON.stringify(details)) : ""
        }),
        keepalive: true
      }).catch(function() {});
    }
  } catch(e) {}
}

var acpIsSwapping = false;

function acpExecuteDirectSwap() {
  if (!acpSelectedSwapImage || !acpTargetSwapSlot) return;
  if (acpIsSwapping) {
    acpShowToast('⏳ <strong>Bildtausch läuft bereits...</strong> Einen kurzen Moment bitte.', 3000);
    return;
  }
  acpIsSwapping = true;

  var btn = document.querySelector(".btn-swap-exec");
  if (btn) {
    btn.disabled = true;
    btn.textContent = "⏳ Tausche & Deploye...";
  }

  var currentJob = getActiveJob();
  var activeFile = (acpTargetSwapSlot && acpTargetSwapSlot.datei) || (currentJob ? currentJob.datei : 'index.html');
  var cleanOld = acpTargetSwapSlot.currentSrc.split('/').pop() || acpTargetSwapSlot.slot;
  var cleanNew = acpSelectedSwapImage.filename;
  acpLog("swap", "🎯 Tauschziel im Inserat gewählt: " + cleanOld + " ➔ " + cleanNew, "Datei: " + activeFile + " · Slot: " + acpTargetSwapSlot.slot);

  acpShowToast('⚡ <strong>Bildtausch gestartet:</strong> Tausche ' + cleanOld + ' ➔ ' + cleanNew + '...<br><small>Cloudflare Pages aktualisiert den Edge-Cache...</small>', 8000);

  var payload = {
    client: currentJob.folder || 'hiltbrand',
    file: activeFile,
    old_path: acpTargetSwapSlot.currentSrc,
    new_path: acpSelectedSwapImage.rel_path,
    is_hero: !!acpTargetSwapSlot.isHero,
    slot: acpTargetSwapSlot.slot || ""
  };

  acpLog("info", "⚡ Sende Tausch an VPS (swap-image)...", "Mandant: " + (payload.client || "") + " · " + cleanOld + " ➔ " + cleanNew);
  fetch("/api/publish-career/swap-image", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(function(res) {
    return res.json().then(function(data) { return { ok: res.ok, data: data }; });
  })
  .then(function(result) {
    acpIsSwapping = false;
    if (result.ok && result.data.ok) {
      // 1. Swap-Dock & Spotlight lautlos schliessen (das Bild bleibt im DOM stabil erhalten!)
      acpCancelSwap(true);
      // 2. Erfolgs-Meldung anzeigen (KEIN zerstörerischer iFrame-Reload!)
      acpLog("success", "🎉 Bildtausch erfolgreich verarbeitet!", "Edge CDN synchronisiert · Datei: " + payload.file);
      acpShowToast('🎉 <strong>Bild erfolgreich getauscht!</strong><br><small><strong>' + cleanNew + '</strong> ist jetzt im HTML fest verankert und weltweit live.</small>', 8000);
    } else {
      var err = (result.data && result.data.error) || 'Fehler beim Bildtausch';
      acpLog("error", "❌ Tausch vom Server abgewiesen: " + err, JSON.stringify(result.data));
      acpShowToast('❌ <strong>Fehler:</strong> ' + err, 7000);
      acpReportClientEvent('error', 'Bildtausch abgelehnt: ' + err, payload);
      if (btn) {
        btn.disabled = false;
        btn.textContent = "⚡ Direkt im HTML tauschen";
      }
    }
  })
  .catch(function(err) {
    acpIsSwapping = false;
    acpShowToast('❌ <strong>Netzwerkfehler:</strong> ' + err.message, 6000);
    acpReportClientEvent('error', 'Netzwerkfehler bei Bildtausch: ' + err.message, payload);
    if (btn) {
      btn.disabled = false;
      btn.textContent = "⚡ Direkt im HTML tauschen";
    }
  });
}

function acpCopyCombinedPrompt() {
  if (!acpSelectedSwapImage || !acpTargetSwapSlot) return;

  var promptText = 'Ersetze in der Datei "' + acpTargetSwapSlot.datei + '" im Slot "' + acpTargetSwapSlot.slot + '" das Bild (' + acpTargetSwapSlot.currentSrc + ') durch das neue Bild "' + acpSelectedSwapImage.rel_path + '".\n\n' +
    'REGELN:\n' +
    '1. Gib ausnahmslos den VOLLSTÄNDIGEN Quellcode von <!DOCTYPE html> bis </html> aus.\n' +
    '2. Keine Kürzungen, keine Auslassungen, keine Platzhalter.\n' +
    '3. Belasse alle Design-Systeme, WhatsApp-Buttons und CSS-Regeln unverändert.';

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(promptText);
  }
  acpShowToast('🤖 <strong>ChatGPT-Kombi-Prompt kopiert!</strong><br><small>Füge den Befehl in ChatGPT oder Gemini ein.</small>', 5000);
  acpCancelSwap();
}

// -------------------------------------------------------
// [3] STELLEN-ZENTRALE & INSERATE-MANAGER
// -------------------------------------------------------
function acpToggleDirectoryModal() {
  var modal = document.getElementById("acp-directory-modal");
  if (!modal) return;
  var isOpen = modal.classList.contains("is-open");
  if (!isOpen) {
    renderDirectoryTable();
    updateSnippetBox();
    modal.classList.add("is-open");
  } else {
    modal.classList.remove("is-open");
  }
  acpUpdateBodyModalClass();
}

function acpSetJobFilter(filter) {
  acpCurrentJobFilter = filter;
  renderDirectoryTable();
}

function acpFilterJobs() {
  renderDirectoryTable();
}

function renderDirectoryTable() {
  var tbody = document.getElementById("acp-directory-tbody");
  if (!tbody) return;

  var searchInput = document.getElementById("acp-jobs-search");
  var query = (searchInput ? searchInput.value : "").toLowerCase().trim();

  var countAll = ACP_STELLEN.length;
  var countLive = ACP_STELLEN.filter(function(j) { return !!j.is_live; }).length;

  // Firmen-Zählung dynamisch ermitteln
  var companyCounts = {};
  ACP_STELLEN.forEach(function(j) {
    var fn = (j.firma || "").trim();
    if (fn) {
      companyCounts[fn] = (companyCounts[fn] || 0) + 1;
    }
  });
  var companyNames = Object.keys(companyCounts);

  // Filter-Pills dynamisch rendern falls Pills-Container vorhanden
  var pillsContainer = document.getElementById("acp-jobs-filter-pills");
  if (pillsContainer) {
    var pillsHtml = '<button type="button" class="acp-job-filter-pill' + (acpCurrentJobFilter === 'alle' ? ' active' : '') + '" data-filter="alle" onclick="acpSetJobFilter(\'alle\')">🏢 Alle Inserate (<span id="count-jobs-all">' + countAll + '</span>)</button>';
    
    if (companyNames.length > 1) {
      companyNames.forEach(function(cName) {
        var isAct = (acpCurrentJobFilter === cName || acpCurrentJobFilter === ('firma:' + cName) || (cName.indexOf('Hiltbrand') !== -1 && acpCurrentJobFilter === 'hiltbrand') || (cName.indexOf('Zurbuchen') !== -1 && acpCurrentJobFilter === 'zurbuchen'));
        var icon = '🏢';
        var cLower = cName.toLowerCase();
        if (cLower.indexOf('holz') !== -1 || cLower.indexOf('zurbuchen') !== -1) icon = '🌲';
        else if (cLower.indexOf('dach') !== -1 || cLower.indexOf('hiltbrand') !== -1 || cLower.indexOf('gebäude') !== -1) icon = '🏠';
        
        pillsHtml += ' <button type="button" class="acp-job-filter-pill' + (isAct ? ' active' : '') + '" data-filter="firma:' + cName + '" onclick="acpSetJobFilter(\'firma:' + cName.replace(/'/g, "\\'") + '\')">' + icon + ' ' + cName + ' (<span>' + companyCounts[cName] + '</span>)</button>';
      });
    }

    pillsHtml += ' <button type="button" class="acp-job-filter-pill' + (acpCurrentJobFilter === 'live' ? ' active' : '') + '" data-filter="live" onclick="acpSetJobFilter(\'live\')">🟢 Nur Live-Widget (<span id="count-jobs-live">' + countLive + '</span>)</button>';
    
    pillsContainer.innerHTML = pillsHtml;
  }

  var filtered = ACP_STELLEN.filter(function(j) {
    if (acpCurrentJobFilter === 'live' && !j.is_live) return false;
    if (acpCurrentJobFilter.indexOf('firma:') === 0) {
      var targetFirma = acpCurrentJobFilter.substring(6);
      if ((j.firma || '').indexOf(targetFirma) === -1) return false;
    }
    if (acpCurrentJobFilter === 'hiltbrand' && (j.firma || '').indexOf('Hiltbrand') === -1) return false;
    if (acpCurrentJobFilter === 'zurbuchen' && (j.firma || '').indexOf('Zurbuchen') === -1) return false;

    if (query) {
      var mFile = (j.datei || '').toLowerCase().indexOf(query) !== -1;
      var mTitle = (j.titel || '').toLowerCase().indexOf(query) !== -1;
      var mFirma = (j.firma || '').toLowerCase().indexOf(query) !== -1;
      return mFile || mTitle || mFirma;
    }
    return true;
  });

  if (filtered.length === 0) {
    tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:48px 20px; color:#64748b; font-family:\'JetBrains Mono\',monospace; font-size:13px;">Keine passenden Stellen gefunden.</td></tr>';
    return;
  }

  var html = "";
  for (var i = 0; i < filtered.length; i++) {
    var j = filtered[i];
    var subfolder = j.folder || (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.slug) || ((j.firma && j.firma.indexOf('Zurbuchen') !== -1) ? 'zurbuchen' : 'hiltbrand');
    var edgePreviewUrl = j.edge_url || ('https://embed.magnet-xs.ch/' + subfolder + '/' + j.datei);
    var cleanEdgeDomain = 'embed.magnet-xs.ch/' + subfolder + '/' + j.datei;

    var isCurrent = (j.id === activeJobId);
    var rowClass = isCurrent ? "is-active-job" : "";
    
    var statusBadge = "";
    if (j.is_live) {
      statusBadge = '<span class="acp-table-badge badge-live"><span class="badge-dot-live">●</span> LIVE</span>';
    } else if (j.id && j.id.indexOf("zurbuchen") !== -1) {
      statusBadge = '<span class="acp-table-badge badge-ready"><span class="badge-dot-ready">●</span> BEREIT</span>';
    } else {
      statusBadge = '<span class="acp-table-badge badge-draft"><span class="badge-dot-draft">●</span> ENTWURF</span>';
    }

    var actionBtn = isCurrent ?
      '<button type="button" class="btn-job-action btn-job-selected" disabled><span class="action-icon">✓</span> Aktiv</button>' :
      '<button type="button" class="btn-job-action btn-job-switch" onclick="acpSwitchJob(\'' + j.id + '\'); acpToggleDirectoryModal();"><span class="action-icon">⚡</span> Auswählen</button>';

    html += '<tr class="' + rowClass + '">' +
      '<td>' +
        '<div class="job-meta-cell">' +
          '<div class="job-title-row">' +
            '<span class="job-icon-glyph">' + (j.icon || "💼") + '</span>' +
            '<strong class="job-title-text">' + j.titel + '</strong>' +
            (isCurrent ? '<span class="job-current-pill">Aktiv</span>' : '') +
          '</div>' +
          '<div class="job-subline-row">' +
            '<span class="job-company-label">' + j.firma + '</span>' +
            '<span class="job-dot-sep">·</span>' +
            '<a href="' + edgePreviewUrl + '" target="_blank" class="job-preview-link" title="Öffentliche Edge-Vorschau im Browser-Tab öffnen">' +
              '<span>' + cleanEdgeDomain + '</span>' +
              '<span class="link-arrow">↗</span>' +
            '</a>' +
          '</div>' +
        '</div>' +
      '</td>' +
      '<td>' +
        statusBadge +
      '</td>' +
      '<td>' +
        '<button type="button" class="job-file-chip" onclick="acpCopyJobFilename(\'' + j.datei + '\')" title="Klicken, um Dateinamen zu kopieren">' +
          '<span class="file-icon">📄</span>' +
          '<span class="file-name">' + j.datei + '</span>' +
          '<span class="file-copy-icon">📋</span>' +
        '</button>' +
      '</td>' +
      '<td style="text-align:right; white-space:nowrap;">' +
        '<div class="job-actions-cluster">' +
          actionBtn +
          '<button type="button" class="btn-job-tool" onclick="acpCopyPreviewUrl(\'' + edgePreviewUrl + '\', \'' + j.titel + '\')" title="Vorschau-Link teilen (WhatsApp / Mail)">🔗</button>' +
          '<button type="button" class="btn-job-tool" onclick="acpCopyJobCode(\'' + j.id + '\')" title="Einbettungs-Code für Webmaster kopieren">📋</button>' +
        '</div>' +
      '</td>' +
    '</tr>';
  }
  tbody.innerHTML = html;
}

function acpCopyPreviewUrl(url, title) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(url);
    acpShowToast('🔗 <strong>Vorschau-Link kopiert!</strong><br><small>' + url + '<br>👉 Ideal zum Teilen per WhatsApp oder E-Mail.</small>', 5000);
  } else {
    window.prompt("Kopiere diesen Vorschau-Link:", url);
  }
}

function acpCopyJobFilename(filename) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(filename);
    acpShowToast('📋 Dateiname <code>' + filename + '</code> kopiert!');
  }
}

// -------------------------------------------------------
// [4] EVENT LISTENER & INSPEKTOR
// -------------------------------------------------------
window.addEventListener("message", function(e) {
  if (e.data && e.data.type === "acp-embed-resize") {
    var frame = document.getElementById("acp-widget-viewport");
    if (frame && e.data.height > 300) {
      frame.style.height = (e.data.height + 10) + "px";
    }
  }
  if (e.data && (e.data.type === "acp-slot-click" || e.data.type === "acp-client-slot-click")) {
    acpHandleSlotClick(e.data);
  }
  if (e.data && e.data.type === "acp-toast") {
    acpShowToast(e.data.text);
  }
  if (e.data && e.data.type === "acp-cancel-swap") {
    acpCancelSwap();
  }
});

function acpToggleMenu() {
  acpMenuOpen = !acpMenuOpen;
  var panel = document.getElementById("acp-draft-panel");
  if (panel) panel.classList.toggle("is-open", acpMenuOpen);
}

function acpToggleInspector() {
  acpInspectorActive = !acpInspectorActive;
  var btn = document.getElementById("acp-btn-inspector");
  if (btn) {
    if (acpInspectorActive) {
      btn.textContent = "AN";
      btn.classList.add("active");
      acpShowToast("🔍 <strong>Klick-Inspektor AN:</strong> Klicke auf ein Bild oder einen Text im Inserat.", 4000);
    } else {
      btn.textContent = "AUS";
      btn.classList.remove("active");
      acpShowToast("Klick-Inspektor AUS");
    }
  }
  var frame = document.getElementById("acp-widget-viewport");
  if (frame && frame.contentWindow) {
    frame.contentWindow.postMessage({ type: "acp-toggle-inspector", active: acpInspectorActive }, "*");
  }
}

function acpShowToast(text, duration) {
  var toast = document.getElementById("acp-toast");
  if (!toast) return;
  toast.innerHTML = text;
  toast.classList.add("is-visible");
  setTimeout(function() {
    toast.classList.remove("is-visible");
  }, duration || 3500);
}

// -------------------------------------------------------
// [5] SCHARFSTELLEN / PUBLISH
// -------------------------------------------------------
function acpPublishLive() {
  var btn = document.getElementById("acp-btn-publish");
  if (!btn || btn.disabled) return;

  btn.disabled = true;
  btn.innerHTML = '<span>⏳ Airbag prüft...</span>';
  btn.style.background = "#d97706";
  btn.style.color = "#ffffff";

  fetch("/api/publish-career", {
    method: "POST",
    headers: { "Content-Type": "application/json" }
  })
  .then(function(res) {
    return res.json().then(function(data) { return { ok: res.ok, data: data }; });
  })
  .then(function(result) {
    if (result.ok && result.data.ok) {
      btn.innerHTML = '<span>✅ Live geschaltet!</span>';
      btn.style.background = "#10b981";
      btn.style.color = "#ffffff";
      var msg = result.data.message || 'In ca. 15 Sekunden live auf WordPress!';
      acpShowToast('🚀 <strong>Erfolgreich scharfgestellt!</strong><br><small>' + msg + '</small>', 6000);
      setTimeout(function() {
        btn.disabled = false;
        btn.innerHTML = '<span>🚀 Jetzt scharfstellen</span>';
        btn.style.background = "";
        btn.style.color = "";
      }, 5000);
    } else {
      var err = (result.data && (result.data.error || result.data.details)) || 'Unbekannter Fehler';
      btn.innerHTML = '<span>⚠️ Fehler beim Deploy</span>';
      btn.style.background = "#ef4444";
      btn.style.color = "#ffffff";
      acpShowToast('⚠️ <strong>Live-Schaltung abgelehnt:</strong><br><small>' + err + '</small>', 8000);
      acpReportClientEvent('error', 'Live-Schaltung abgelehnt: ' + err);
      setTimeout(function() {
        btn.disabled = false;
        btn.innerHTML = '<span>🚀 Jetzt scharfstellen</span>';
        btn.style.background = "";
        btn.style.color = "";
      }, 6000);
    }
  })
  .catch(function(err) {
    btn.innerHTML = '<span>❌ Verbindungsfehler</span>';
    btn.style.background = "#ef4444";
    btn.style.color = "#ffffff";
    acpShowToast('❌ <strong>Netzwerkfehler:</strong> Konnte den Server nicht erreichen.<br><small>' + err.message + '</small>', 6000);
    acpReportClientEvent('error', 'Verbindungsfehler bei Live-Schaltung: ' + err.message);
    setTimeout(function() {
      btn.disabled = false;
      btn.innerHTML = '<span>🚀 Jetzt scharfstellen</span>';
      btn.style.background = "";
      btn.style.color = "";
    }, 5000);
  });
}

// -------------------------------------------------------
// [6] INITIALISIERUNG
// -------------------------------------------------------
function checkEnvironmentAndRender() {
  var isOnline = (window.location.protocol === "http:" || window.location.protocol === "https:");
  var badgeLabel = document.getElementById("acp-brand-label");
  var brandBadge = document.getElementById("acp-brand-badge");
  var onlineBtn = document.getElementById("acp-online-btn");

  if (isOnline) {
    if (badgeLabel) badgeLabel.textContent = "KARRIERE-STUDIO";
    if (brandBadge) {
      brandBadge.title = "Magnet-XS Karriere-Studio (Online auf Cloudflare Pages)";
    }
    if (onlineBtn) {
      onlineBtn.innerHTML = '<span class="nav-icon">🔗</span><span class="nav-label">Link</span>';
      onlineBtn.title = "Link zu diesem Online-Cockpit in die Zwischenablage kopieren";
      onlineBtn.onclick = function(e) {
        e.preventDefault();
        acpCopyOnlineUrl(onlineBtn);
      };
    }
  } else {
    if (badgeLabel) badgeLabel.textContent = "KARRIERE-STUDIO";
    if (onlineBtn) {
      onlineBtn.href = "https://embed.magnet-xs.ch/hiltbrand/cockpit";
      onlineBtn.target = "_blank";
      onlineBtn.innerHTML = '<span class="nav-icon">🌐</span><span class="nav-label">Online</span>';
      onlineBtn.title = "Online-Cockpit auf embed.magnet-xs.ch öffnen";
    }
  }
}

function setupActiveJobAndRender() {
  var params = new URLSearchParams(window.location.search);
  var jobParam = params.get("stelle") || params.get("job");
  if (jobParam) {
    for (var i = 0; i < ACP_STELLEN.length; i++) {
      if (ACP_STELLEN[i].id === jobParam || ACP_STELLEN[i].datei.toLowerCase().indexOf(jobParam.toLowerCase()) !== -1) {
        activeJobId = ACP_STELLEN[i].id;
        break;
      }
    }
  }
  if (!activeJobId && ACP_STELLEN.length > 0) {
    for (var k = 0; k < ACP_STELLEN.length; k++) {
      if (ACP_STELLEN[k].is_live) {
        activeJobId = ACP_STELLEN[k].id;
        break;
      }
    }
    if (!activeJobId) {
      activeJobId = ACP_STELLEN[0].id;
    }
  }
  checkEnvironmentAndRender();
  renderJobPicker();
  renderDirectoryTable();
  if (activeJobId) {
    acpSwitchJob(activeJobId);
  }
}

function acpInit() {
  console.log("🚀 Magnet-XS Karriere-Cockpit " + ACP_COCKPIT_VERSION + " [Build " + ACP_COCKPIT_BUILD + "] geladen.");
  acpInitUploadDropzone();
  var statusBox = document.getElementById("acp-upload-status");
  if (statusBox) statusBox.classList.remove("is-active");
  if (window.location.protocol === "http:" || window.location.protocol === "https:") {
    acpRefreshImages();
    fetch("stellen.json?t=" + Date.now())
      .then(function(res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function(data) {
        if (Array.isArray(data) && data.length > 0) {
          ACP_STELLEN = sanitizeStellen(data);
        }
        setupActiveJobAndRender();
      })
      .catch(function(err) {
        console.warn("Nutze statische Fallback-Stellen:", err.message);
        setupActiveJobAndRender();
      });
  } else {
    setupActiveJobAndRender();
  }
}

window.addEventListener("DOMContentLoaded", acpInit);


// =======================================================
// [SEKTIONEN & KI-BAUKASTEN] FULL-CONTEXT ENVELOPE ENGINE
// =======================================================
var acpSectionsModalOpen = false;
var acpScannedSections = [];
var acpActiveEditSectionId = null;

function acpToggleSectionsModal() {
  acpSectionsModalOpen = !acpSectionsModalOpen;
  var modal = document.getElementById("acp-sections-modal");
  if (modal) modal.classList.toggle("is-open", acpSectionsModalOpen);
  acpUpdateBodyModalClass();
  if (acpSectionsModalOpen) {
    acpScanAndRenderSections();
  }
}

function acpScanAndRenderSections() {
  var iframe = document.getElementById("acp-widget-viewport");
  var grid = document.getElementById("acp-sections-grid");
  var badge = document.getElementById("acp-sections-count-badge");
  if (!grid) return;

  grid.innerHTML = '<div style="color:var(--grau); padding:20px;">Lese Sektionen aus der Live-Bühne ein...</div>';

  var doc = null;
  try {
    if (iframe && (iframe.contentDocument || iframe.contentWindow)) {
      doc = iframe.contentDocument || iframe.contentWindow.document;
    }
  } catch(e) {
    console.warn("Iframe Zugriff eingeschränkt:", e);
  }

  acpScannedSections = [];

  if (doc) {
    var elements = doc.querySelectorAll("[data-section], section, header.site-header, footer.site-footer, .header-wrap, .footer-wrap");
    elements.forEach(function(el, idx) {
      var id = el.getAttribute("data-section") || el.id || el.tagName.toLowerCase();
      if (id === "acp-cockpit-bar" || el.closest(".acp-cockpit-bar")) return;
      if (acpScannedSections.some(function(s) { return s.id === id; })) return;

      var kicker = el.querySelector(".section-kicker, .hero-kicker, .kicker, .tag");
      var title = el.querySelector(".section-title, .hero-title, h1, h2, h3");

      var kickerText = kicker ? kicker.innerText.trim() : "";
      var titleText = title ? title.innerText.trim() : (el.getAttribute("aria-label") || id);

      var lines = el.outerHTML.split("\n").length;
      var charCount = el.outerHTML.length;

      acpScannedSections.push({
        id: id,
        tag: el.tagName.toLowerCase(),
        kicker: kickerText,
        title: titleText,
        lines: lines,
        chars: charCount,
        outerHTML: el.outerHTML,
        index: idx
      });
    });
  }

  if (acpScannedSections.length === 0) {
    acpScannedSections = [
      { id: "hero", kicker: "Meisterbetrieb in 3. Generation", title: "Gebäudehüllen & Photovoltaik", lines: 120, chars: 4800, outerHTML: '<section class="section-wrap hero-wrap" data-section="hero">...</section>' },
      { id: "services", kicker: "Kompetenzen & Handwerk", title: "Unsere Kernleistungen im Berner Oberland", lines: 95, chars: 3600, outerHTML: '<section class="section-wrap" data-section="services">...</section>' },
      { id: "stories", kicker: "Direkt aus der Praxis", title: "Aktuelle Baustellen & Referenzen", lines: 80, chars: 3100, outerHTML: '<section class="section-wrap" data-section="stories">...</section>' },
      { id: "ratgeber", kicker: "Fachwissen & Ratgeber", title: "Wissen direkt vom Gebäudehüllen-Meister", lines: 75, chars: 2900, outerHTML: '<section class="section-wrap" data-section="ratgeber">...</section>' },
      { id: "team_teaser", kicker: "Menschen & Handwerk", title: "Das Team der Hiltbrand Gebäudehüllen AG", lines: 85, chars: 3400, outerHTML: '<section class="section-wrap" data-section="team_teaser">...</section>' },
      { id: "kontakt", kicker: "Direktkontakt & 24h-Pikett", title: "Offerte anfordern & Kontakt", lines: 110, chars: 4200, outerHTML: '<section class="section-wrap" data-section="kontakt">...</section>' }
    ];
  }

  if (badge) {
    badge.textContent = "● " + acpScannedSections.length + " Sektionen aktiv";
  }

  grid.innerHTML = "";
  acpScannedSections.forEach(function(sec, idx) {
    var card = document.createElement("div");
    card.className = "acp-section-card";
    card.style.cssText = "background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 16px;";

    var isSystem = (sec.id === "header" || sec.id === "footer");
    var badgeColor = isSystem ? "rgba(148, 163, 184, 0.2)" : "rgba(245, 158, 11, 0.15)";
    var badgeText = isSystem ? "SYSTEM" : "SEKTION " + (idx + 1);
    var badgeTextColor = isSystem ? "#94a3b8" : "#fbbf24";

    card.innerHTML = 
      '<div>' +
        '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">' +
          '<span style="font-family:\'JetBrains Mono\',monospace; font-size:11px; font-weight:700; background:' + badgeColor + '; color:' + badgeTextColor + '; padding:3px 8px; border-radius:4px;">' + badgeText + '</span>' +
          '<span style="font-family:\'JetBrains Mono\',monospace; font-size:11px; color:#64748b;">data-section="' + sec.id + '"</span>' +
        '</div>' +
        (sec.kicker ? '<div style="font-family:\'JetBrains Mono\',monospace; font-size:11px; color:#f59e0b; margin-bottom:4px;">' + sec.kicker + '</div>' : '') +
        '<h4 style="color:#fff; font-size:16px; font-weight:700; line-height:1.4; margin-bottom:8px;">' + sec.title + '</h4>' +
        '<div style="font-size:12px; color:#64748b;">' + sec.lines + ' Zeilen · ca. ' + Math.round(sec.chars / 100) / 10 + ' KB Quelltext</div>' +
      '</div>' +
      '<div style="display:flex; gap:8px; flex-wrap:wrap; padding-top:12px; border-top:1px solid rgba(255,255,255,0.08);">' +
        '<button type="button" class="acp-btn-secondary" onclick="acpCopySectionPrompt(\'' + sec.id + '\')" style="flex:1; padding:8px 12px; font-size:12.5px; justify-content:center;" title="Kopiert Prompt inkl. vollem Seiten-Kontext">' +
          '<span>📋 Prompt kopieren</span>' +
        '</button>' +
        '<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal(\'' + sec.id + '\')" style="padding:8px 12px; font-size:12.5px;" title="Modifizierten KI-Code einfügen">' +
          '<span>✏️ Ersetzen</span>' +
        '</button>' +
        (!isSystem ? '<button type="button" class="acp-btn-secondary" onclick="acpRemoveSection(\'' + sec.id + '\')" style="padding:8px 10px; font-size:12.5px; color:#ef4444; border-color:rgba(239,68,68,0.3);" title="Sektion entfernen"><span>🗑️</span></button>' : '') +
      '</div>';

    grid.appendChild(card);
  });
}

function acpBuildFullContextEnvelope(targetSecId, customGoal) {
  var targetSec = acpScannedSections.find(function(s) { return s.id === targetSecId; });
  if (!targetSec) return "";

  var sectionsOutline = acpScannedSections.map(function(s, i) {
    return "   " + (i + 1) + ". [" + s.id + "] " + (s.kicker ? s.kicker + " · " : "") + s.title;
  }).join("\n");

  var targetIdx = acpScannedSections.findIndex(function(s) { return s.id === targetSecId; });
  var prevSec = targetIdx > 0 ? acpScannedSections[targetIdx - 1] : null;
  var nextSec = targetIdx < acpScannedSections.length - 1 ? acpScannedSections[targetIdx + 1] : null;

  var prevInfo = prevSec ? "Liegt direkt NACH: [" + prevSec.id + "] " + prevSec.title : "Liegt ganz oben auf der Seite (Hero-Bereich)";
  var nextInfo = nextSec ? "Liegt direkt VOR: [" + nextSec.id + "] " + nextSec.title : "Liegt direkt vor dem Footer";

  var profile = window.ACP_CLIENT_PROFILE || {};
  var industryLabel = profile.industry_label || "Schweizer Unternehmens-Website";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Fachspezialisten EFZ\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\").";

  var prompt = 
"Du bist mein technischer Web-Entwickler für meine " + industryLabel + " (WebPilot Obsidian-Dark Design).\n" +
"Ich möchte die Sektion \"" + targetSec.title + "\" (data-section=\"" + targetSec.id + "\") anpassen.\n\n" +

"================================================================================\n" +
"1. GESAMT-KONTEXT DER SEITE (FÜR TONALITÄT, STIMMIGKEIT & FLOW):\n" +
"================================================================================\n" +
"- Vorhandene Abschnitte auf dieser Seite:\n" + sectionsOutline + "\n\n" +
"- Position dieser Sektion im Fluss der Seite:\n" +
"  * " + prevInfo + "\n" +
"  * " + nextInfo + "\n\n" +

"================================================================================\n" +
"2. VERBINDLICHE SCHWEIZER SPRACH- & DESIGN-DOKTRIN:\n" +
"================================================================================\n" +
"- Sprache: Authentisches Schweizer Hochdeutsch (100% Verbot von \"ß\", nutze \"ss\").\n" +
promptRules + "\n" +
"- Schweizer Typografie: Nutze die bestehenden Klassen (.section-wrap, .section-inner, .section-kicker, .section-title, .section-desc).\n" +
"- Kicker-Regel: <span class=\"section-kicker\">● Kicker-Text</span> ist 100% freistehend (keine Box, kein Badge-Rahmen).\n" +
"- Zero-Emoji: Keine bunten Emojis in Überschriften oder Badges.\n" +
"- Bilder: Bildpfade zeigen auf \"images/[dateiname.jpg]\".\n\n" +

"================================================================================\n" +
"3. AKTUELLER QUELLCODE DIESER SEKTION (ZUR BEARBEITUNG):\n" +
"================================================================================\n" +
targetSec.outerHTML + "\n\n" +

"================================================================================\n" +
"4. MEIN ÄNDERUNGSWUNSCH:\n" +
"================================================================================\n" +
(customGoal ? customGoal : "[Hier konkreten Änderungswunsch eingeben, z.B. Text umschreiben, Vorteil anpassen, 4. Bildkarte hinzufügen]") + "\n\n" +

"================================================================================\n" +
"AUSGABE-REGEL (GOLDENE REGEL):\n" +
"================================================================================\n" +
"Nutze den gesamten Kontext für Tonalität und Flow, aber gib mir als Antwort AUSSCHLIESSLICH den vollständigen, sauberen HTML-Code von <section ...> bis </section> im Codeblock aus.\n" +
"Schliesse ausnahmslos alle Tags (<div>, <section>, <p>, <span>) sauber ab. Keine Auslassungen (wie // ... restlicher Code ...)!";

  return prompt;
}

function acpCopySectionPrompt(secId) {
  var promptText = acpBuildFullContextEnvelope(secId, "");
  if (!promptText) return;
  navigator.clipboard.writeText(promptText).then(function() {
    alert("✓ Vollständiger Prompt für Sektion [" + secId + "] inklusive Gesamt-Kontext in die Zwischenablage kopiert!\n\nJetzt einfach in ChatGPT oder Claude einfügen.");
  }).catch(function() {
    window.prompt("Kopiere diesen Prompt für ChatGPT / Claude:", promptText);
  });
}

function acpCopyFullPagePrompt() {
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  var fullHtml = doc ? doc.documentElement.outerHTML : "";
  if (!fullHtml) {
    alert("Konnte den Quellcode der Seite nicht einlesen.");
    return;
  }
  var profile = window.ACP_CLIENT_PROFILE || {};
  var industryLabel = profile.industry_label || "Schweizer Unternehmens-Website";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Fachspezialisten EFZ\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\").";

  var prompt = 
"Du bist mein technischer Web-Redakteur für meine " + industryLabel + ".\n" +
"Ich übergebe dir hier den VOLLSTÄNDIGEN Quellcode meiner Website (HTML5).\n\n" +
"MEINE REGELN:\n" +
"1. Schweizer Hochdeutsch (0x 'ß', Schweizer Fachbegriffe):\n" +
promptRules + "\n" +
"2. Schweizer Obsidian-Design & bestehende Klassen beibehalten.\n" +
"3. AUSGABE-PFLICHT: Gib mir den Quellcode immer als eine einzige, vollständige und ungekürzte HTML-Datei aus – ausnahmslos von <!DOCTYPE html> bis </html>. Verwende keine Code-Auslassungen!\n\n" +
"QUELLCODE:\n" + fullHtml;

  navigator.clipboard.writeText(prompt).then(function() {
    alert("✓ Komplette HTML-Seite inklusive Master-Prompt kopiert!");
  }).catch(function() {
    window.prompt("Kopiere die ganze Seite:", prompt);
  });
}

function acpOpenReplaceSectionModal(secId) {
  acpActiveEditSectionId = secId;
  var modal = document.getElementById("acp-replace-section-modal");
  var title = document.getElementById("acp-replace-modal-title");
  var textarea = document.getElementById("acp-replace-code-input");
  var status = document.getElementById("acp-replace-airbag-status");
  if (status) status.style.display = "none";
  if (title) title.textContent = "Sektion [" + secId + "] bearbeiten & ersetzen";
  if (textarea) textarea.value = "";
  if (modal) modal.style.display = "block";
}

function acpCloseReplaceSectionModal() {
  var modal = document.getElementById("acp-replace-section-modal");
  if (modal) modal.style.display = "none";
}

function acpValidateSectionHtml(html) {
  if (!html || !html.trim()) {
    return { ok: false, error: "Der Code ist leer!" };
  }
  var clean = html.trim();
  if (!clean.startsWith("<section") || !clean.endsWith("</section>")) {
    return { ok: false, error: "Der Code muss mit <section ...> beginnen und mit </section> enden." };
  }

  // 1. Gefährliche / ausführbare Tags deterministisch blockieren (White-Hat Airbag)
  var forbiddenTags = /<(script|iframe|object|embed|form|meta|base|style)\b[^>]*>/i;
  var mTag = clean.match(forbiddenTags);
  if (mTag) {
    return { ok: false, error: "Sicherheits-Schranke: Ausführbare Tags (<" + mTag[1] + ">) sind in Inhalts-Sektionen verboten." };
  }

  // 2. Inline Event-Handler blockieren (onerror, onload, onclick, onmouseover etc.)
  if (/\son[a-zA-Z]+\s*=/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: Inline-JavaScript (on... Event-Handler wie onerror, onclick) ist aus Sicherheitsgründen verboten." };
  }

  // 3. Pseudo-Protokolle (javascript:, data:text/html) blockieren
  if (/(href|src|action)\s*=\s*["'\s]*javascript:/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: javascript:... URLs sind aus Sicherheitsgründen verboten." };
  }
  if (/(href|src)\s*=\s*["'\s]*data:text\/html/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: data:text/html URLs sind nicht erlaubt." };
  }

  // 4. Tag-Balancierung
  var checkTags = ["section", "div", "p", "span", "a", "h2", "h3", "h4", "ul", "ol", "li"];
  for (var i = 0; i < checkTags.length; i++) {
    var tag = checkTags[i];
    var openRegex = new RegExp("<" + tag + "(\s+[^>]*)?>", "gi");
    var closeRegex = new RegExp("</" + tag + ">", "gi");
    var openCount = (clean.match(openRegex) || []).length;
    var closeCount = (clean.match(closeRegex) || []).length;
    if (openCount !== closeCount) {
      return { 
        ok: false, 
        error: "Tag-Fehler bei <" + tag + ">: Wurde " + openCount + "x geöffnet, aber " + closeCount + "x geschlossen. Bitte sag ChatGPT: 'Schliesse alle <" + tag + "> Tags sauber ab!'" 
      };
    }
  }

  return { ok: true, html: clean };
}

function acpSubmitReplaceSection() {
  var textarea = document.getElementById("acp-replace-code-input");
  var status = document.getElementById("acp-replace-airbag-status");
  if (!textarea || !textarea.value) return;

  var validation = acpValidateSectionHtml(textarea.value);
  if (!validation.ok) {
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "🚨 <strong>Airbag-Schranke:</strong> " + validation.error;
    }
    return;
  }

  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) {
    alert("Iframe nicht verfügbar!");
    return;
  }

  var targetEl = doc.querySelector('[data-section="' + acpActiveEditSectionId + '"]') || doc.getElementById(acpActiveEditSectionId);
  if (!targetEl) {
    alert("Ziel-Sektion [" + acpActiveEditSectionId + "] nicht im Dokument gefunden!");
    return;
  }

  var temp = doc.createElement("div");
  temp.innerHTML = validation.html;
  var newSecEl = temp.firstElementChild;

  targetEl.parentNode.replaceChild(newSecEl, targetEl);
  acpCloseReplaceSectionModal();
  acpScanAndRenderSections();
  alert("✓ Sektion [" + acpActiveEditSectionId + "] erfolgreich aktualisiert!");
}

function acpOpenNewSectionModal() {
  var modal = document.getElementById("acp-new-section-modal");
  var select = document.getElementById("acp-new-sec-position");
  var status = document.getElementById("acp-new-airbag-status");
  if (status) status.style.display = "none";

  if (select) {
    select.innerHTML = "";
    acpScannedSections.forEach(function(s) {
      var opt = document.createElement("option");
      opt.value = s.id;
      opt.textContent = "Nach [" + s.id + "] " + s.title;
      select.appendChild(opt);
    });
  }
  if (modal) modal.style.display = "block";
}

function acpCloseNewSectionModal() {
  var modal = document.getElementById("acp-new-section-modal");
  if (modal) modal.style.display = "none";
}

function acpCopyGeneratedNewSectionPrompt() {
  var select = document.getElementById("acp-new-sec-position");
  var topicInput = document.getElementById("acp-new-sec-topic");
  var pos = select ? select.value : "services";
  var topic = topicInput && topicInput.value ? topicInput.value : "Unsere Partnerbetriebe & Netzwerke";

  var afterSec = acpScannedSections.find(function(s) { return s.id === pos; }) || acpScannedSections[0];
  var slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

  var profile = window.ACP_CLIENT_PROFILE || {};
  var industryLabel = profile.industry_label || "Schweizer Unternehmens-Website";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Fachspezialisten EFZ\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\").";

  var prompt = 
"Du bist mein technischer Web-Entwickler für meine " + industryLabel + " (WebPilot Obsidian-Dark Design).\n" +
"Erstelle mir eine NEUE HTML5-Sektion für folgendes Thema:\n" +
"\"" + topic + "\"\n\n" +

"================================================================================\n" +
"1. POSITIONIERUNG & GESAMT-KONTEXT DER SEITE:\n" +
"================================================================================\n" +
"- Die neue Sektion wird direkt nach [" + afterSec.id + "] \"" + afterSec.title + "\" eingehängt.\n" +
"- Sie muss sich nahtlos in das Obsidian-Dark Theme (#0b0f19 Canvas, Platin-Text, Bernstein/Gold Akzente) einfügen.\n\n" +

"================================================================================\n" +
"2. STRUKTUR- & CSS-VORGABEN:\n" +
"================================================================================\n" +
"- Root-Tag: <section class=\"section-wrap\" data-section=\"" + slug + "\" id=\"" + slug + "\">\n" +
"- Inner-Container: <div class=\"section-inner\">\n" +
"- Kicker: <span class=\"section-kicker\">● THEMA</span> (11px JetBrains Mono, freistehend, kein Rahmen)\n" +
"- Titel: <h2 class=\"section-title\">Prägnante Überschrift</h2>\n" +
"- Untertitel: <p class=\"section-desc\">Kurze, vertrauensbildende Beschreibung.</p>\n" +
"- Grid: Responsives CSS-Grid mit style=\"display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px;\"\n" +
"- Sprache & Fachbegriffe:\n" + promptRules + "\n" +
"- Emojis: 0 bunte Emojis.\n\n" +

"================================================================================\n" +
"AUSGABE-REGEL:\n" +
"================================================================================\n" +
"Gib mir als Antwort AUSSCHLIESSLICH den fertigen, validen HTML-Code von <section ...> bis </section> im Codeblock aus.\n" +
"Alle Tags müssen zwingend vollständig geschlossen sein!";

  navigator.clipboard.writeText(prompt).then(function() {
    alert("✓ Neuer Sektions-Prompt mit Schweizer Design-Vorgaben kopiert!\n\nJetzt in ChatGPT oder Claude einfügen.");
  }).catch(function() {
    window.prompt("Kopiere diesen Prompt:", prompt);
  });
}

function acpSubmitNewSection() {
  var textarea = document.getElementById("acp-new-sec-code-input");
  var select = document.getElementById("acp-new-sec-position");
  var status = document.getElementById("acp-new-airbag-status");
  if (!textarea || !textarea.value) return;

  var validation = acpValidateSectionHtml(textarea.value);
  if (!validation.ok) {
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "🚨 <strong>Airbag-Schranke:</strong> " + validation.error;
    }
    return;
  }

  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) {
    alert("Iframe nicht verfügbar!");
    return;
  }

  var afterSecId = select ? select.value : "services";
  var targetEl = doc.querySelector('[data-section="' + afterSecId + '"]') || doc.getElementById(afterSecId);
  if (!targetEl) {
    alert("Ziel-Sektion [" + afterSecId + "] nicht im Dokument gefunden!");
    return;
  }

  var temp = doc.createElement("div");
  temp.innerHTML = validation.html;
  var newSecEl = temp.firstElementChild;

  targetEl.parentNode.insertBefore(newSecEl, targetEl.nextSibling);
  acpCloseNewSectionModal();
  acpScanAndRenderSections();
  alert("✓ Neue Sektion erfolgreich nach [" + afterSecId + "] eingehängt!");
}

function acpRemoveSection(secId) {
  if (!confirm("Möchtest du die Sektion [" + secId + "] wirklich ausblenden?")) return;
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) return;

  var targetEl = doc.querySelector('[data-section="' + secId + '"]') || doc.getElementById(secId);
  if (targetEl) {
    targetEl.remove();
    acpScanAndRenderSections();
    alert("✓ Sektion [" + secId + "] entfernt!");
  }
}



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
  var clientSlug = (currentJob && currentJob.folder) || (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.slug) || 'preview-birchmeier';
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
var ACP_CLIENT_PROFILE = /* __CLIENT_PROFILE_JSON__ */;

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
var acpClickedTargetElement = null; // Direktes iFrame-DOM-Element für chirurgischen Bildtausch
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

function acpCleanUrlLabel(u) {
  if (!u) return "";
  var s = String(u);
  var protoIdx = s.indexOf("://");
  if (protoIdx !== -1) {
    s = s.substring(protoIdx + 3);
  }
  if (s.charAt(s.length - 1) === "/") {
    s = s.substring(0, s.length - 1);
  }
  return s;
}

function updateLiveStatusBadge(job) {
  var wrap = document.getElementById("acp-live-badge-wrap");
  if (!wrap) return;
  if (!job) { wrap.innerHTML = ""; return; }
  
  if (job.is_live) {
    var url = job.embedded_page_url || job.live_url || "https://dachdecker-berneroberland.ch/jobs/";
    var domain = job.embedded_page_label || (job.host_label || acpCleanUrlLabel(url));
    wrap.innerHTML = '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="acp-live-status-pill is-live" title="Dieses Inserat ist öffentlich als Live-Widget eingebaut auf: ' + url + ' (Klicken, um Seite im neuen Tab zu öffnen)">' +
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
    wrap.innerHTML = '<span class="acp-live-status-pill is-draft" title="Dieser Entwurf ist noch in keiner Website als Widget eingebaut. Er steht bereit im Studio zur Bearbeitung und Einbettung.">' +
      '<span class="acp-draft-dot"></span>' +
      '<span>ENTWURF · Nicht eingebettet</span>' +
    '</span>';
  }
}
window.acpUpdateLiveBadge = updateLiveStatusBadge;

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
    var targetLineHtml = "";
    if (j.is_live) {
      badgeHtml = '<span class="acp-badge-mini live">🟢 LIVE WIDGET</span>';
      var tgt = j.embedded_page_label || (j.embedded_page_url ? acpCleanUrlLabel(j.embedded_page_url) : 'Eingebaut');
      targetLineHtml = '<div class="dropdown-item-target is-live" title="' + (j.embedded_page_url || '') + '"><span class="target-bullet">↗</span> <span>Eingebaut: ' + tgt + '</span></div>';
    } else if (j.id && j.id.indexOf("zurbuchen") !== -1) {
      badgeHtml = '<span class="acp-badge-mini ready">🟡 BEREIT</span>';
      targetLineHtml = '<div class="dropdown-item-target is-ready"><span class="target-bullet">○</span> <span>Bereit zur Einbettung</span></div>';
    } else {
      badgeHtml = '<span class="acp-badge-mini draft">⚪ ENTWURF</span>';
      targetLineHtml = '<div class="dropdown-item-target is-draft"><span class="target-bullet">○</span> <span>Entwurf · Nicht eingebaut</span></div>';
    }

    html += '<div class="acp-dropdown-item ' + activeClass + '" onclick="acpSwitchJob(\'' + j.id + '\'); acpToggleJobDropdown();">' +
      '<div class="dropdown-item-left">' +
        '<div class="dropdown-item-title">' + (j.icon || "💼") + ' ' + j.titel + '</div>' +
        '<div class="dropdown-item-meta"><span>' + j.firma + '</span> · <span class="dropdown-file-name">' + j.datei + '</span></div>' +
        targetLineHtml +
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
  if (acpSyncPollTimer) {
    clearTimeout(acpSyncPollTimer);
    acpSyncPollTimer = null;
  }
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
  var profileSlug = (typeof ACP_CLIENT_PROFILE !== "undefined" && ACP_CLIENT_PROFILE.slug) ? ACP_CLIENT_PROFILE.slug : "";
  var subfolder = job.folder || profileSlug || ((job.firma && job.firma.indexOf("Zurbuchen") !== -1) ? "zurbuchen" : "hiltbrand");
  var cleanClient = profileSlug.replace("preview-", "") || subfolder.replace("preview-", "");
  var edgePreviewUrl = job.edge_url || ("https://embed.magnet-xs.ch/" + subfolder + "/" + job.datei);

  var curToken = new URLSearchParams(window.location.search).get("token");
  var isDirectHost = (window.location.origin.indexOf("vorschau.magnet-xs.ch") !== -1);
  var cleanPage = (job.datei || "index.html").replace(/\.html$/, "");
  if (cleanPage === "index") cleanPage = "";

  var targetLiveUrl = "";
  var displayUrl = "";

  if (job.embedded_page_url || (job.is_live && job.live_url)) {
    targetLiveUrl = job.embedded_page_url || job.live_url;
    displayUrl = targetLiveUrl.replace(/^https?:\/\//, "");
  } else if (isDirectHost) {
    targetLiveUrl = window.location.origin + "/" + cleanClient + "/" + (cleanPage ? cleanPage : "");
    if (curToken) {
      targetLiveUrl += (targetLiveUrl.indexOf("?") === -1 ? "?token=" : "&token=") + encodeURIComponent(curToken);
    }
    displayUrl = window.location.origin.replace(/^https?:\/\//, "") + "/" + cleanClient + "/" + (cleanPage ? cleanPage : "");
  } else {
    targetLiveUrl = edgePreviewUrl;
    if (curToken && targetLiveUrl.indexOf("token=") === -1) {
      targetLiveUrl += (targetLiveUrl.indexOf("?") === -1 ? "?token=" : "&token=") + encodeURIComponent(curToken);
    }
    displayUrl = edgePreviewUrl.replace(/^https?:\/\//, "");
  }

  if (stageUrl) stageUrl.textContent = displayUrl;
  if (stageLink) {
    stageLink.href = targetLiveUrl;
    stageLink.title = "Seite im neuen Tab öffnen (" + targetLiveUrl + ")";
  }
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
        if (window.location.hostname.indexOf("vorschau.") !== -1) {
          var cleanClient = subfolder.replace(/^preview-/, "");
          var cleanPage = job.datei.replace(/\.html$/, "");
          base = window.location.origin + "/" + cleanClient + "/" + cleanPage;
        } else if (base.indexOf("embed.magnet-xs.ch") !== -1 && base.endsWith(".html")) {
          base = base.replace(/\.html$/, "");
        }
        var curToken = new URLSearchParams(window.location.search).get("token");
        targetSrc = base + (base.indexOf("?") === -1 ? "?embed=true" : "&embed=true");
        if (curToken && targetSrc.indexOf("token=") === -1) {
          targetSrc += "&token=" + encodeURIComponent(curToken);
        }
      }
      if (forceReload) {
        var sep = targetSrc.indexOf("?") === -1 ? "?" : "&";
        targetSrc += sep + "t=" + Date.now();
      }
      frame.src = targetSrc;
      frame.onload = function() {
        frame.style.opacity = "1";
        if (acpInspectorActive) {
          frame.contentWindow.postMessage({ type: "acp-toggle-inspector", active: true }, "*");
        }
        if (acpSelectedSwapImage) {
          acpDispatchSwapMode(true);
          acpRenderSwapDockTargets();
        }
      };
    } else {
      // Job ist bereits aktiv geladen: iFrame NICHT neu laden, damit Bildtausch-Vorschau nicht zurückspringt!
      if (acpInspectorActive && frame.contentWindow) {
        frame.contentWindow.postMessage({ type: "acp-toggle-inspector", active: true }, "*");
      }
      if (acpSelectedSwapImage && frame.contentWindow) {
        acpDispatchSwapMode(true);
        acpRenderSwapDockTargets();
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
  var url = window.location.href;
  if (window.location.protocol === "file:" && typeof ACP_CLIENT_PROFILE !== "undefined" && ACP_CLIENT_PROFILE.host_url) {
    url = ACP_CLIENT_PROFILE.host_url;
  }
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

  var currentJob = getActiveJob();
  var clientSlug = (currentJob && currentJob.folder) || (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.slug) || "preview-birchmeier";

  var fd = new FormData();
  fd.append("file", file);
  fd.append("client", clientSlug);

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

  var currentJob = getActiveJob();
  var clientSlug = (currentJob && currentJob.folder) || (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.slug) || "preview-birchmeier";

  fetch("/api/publish-career/delete-image", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ rel_path: relPath, client: clientSlug })
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

  if (!doc._acpSwapListenerAttached) {
    doc._acpSwapListenerAttached = true;
    doc.addEventListener("click", function(e) {
      if (!acpSelectedSwapImage) return;
      var targetImg = e.target.closest ? e.target.closest("img") : null;
      var targetHero = e.target.closest ? e.target.closest(".hero, [data-slot*='hero']") : null;
      var thisDocFile = (doc.location && doc.location.pathname) ? doc.location.pathname.split("/").pop().split("?")[0] : "";
      if (targetImg) {
        e.preventDefault();
        e.stopPropagation();
        acpClickedTargetElement = targetImg;
        var src = (targetImg.getAttribute("src") || "").replace(/['"]/g, "").split("?")[0].trim();
        var slot = targetImg.getAttribute("data-slot") || targetImg.id || (src.split("/").pop() || "image");
        var isHero = (targetImg.classList && targetImg.classList.contains("hero")) || src.indexOf("hero") !== -1;

        // Kontext-Ermittlung zur eindeutigen Isolierung (Name, Alt-Attribut, Slot)
        var card = targetImg.closest ? targetImg.closest(".member-card, .team-card, .team-upload-box, [data-slot], [data-member-id], article, section, div") : null;
        var nameEl = card ? card.querySelector(".member-name, [id*='Name'], [name*='name'], h2, h3, h4, strong") : null;
        var slotContext = targetImg.getAttribute("alt") || (nameEl ? (nameEl.value || nameEl.textContent || "").trim() : "") || targetImg.id || "";

        acpSelectTargetDirect(src, slot, isHero, thisDocFile, slotContext);
      } else if (targetHero) {
        e.preventDefault();
        e.stopPropagation();
        acpClickedTargetElement = targetHero;
        acpSelectTargetDirect("images/hero.jpg", "hero.hintergrund.bild", true, thisDocFile, "hero");
      }
    }, true);

    doc.addEventListener("keydown", function(e) {
      if (e.key === "Escape" && acpSelectedSwapImage) {
        acpCancelSwap();
      }
    }, true);
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

function acpRenderSwapDockTargets() {
  var targetHint = document.getElementById("acp-swap-target-hint");
  if (!targetHint) return;
  var currentJob = getActiveJob();
  var activeFile = (currentJob && currentJob.datei) || "index.html";
  var usedImages = getUsedImagesForCurrentJob();
  if (usedImages.length > 0) {
    var btnsHtml = '<div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">' +
      '<span style="color:#facc15; font-size:12px; font-weight:700;">👉 Wähle das zu ersetzende Bild:</span>';
    for (var u = 0; u < usedImages.length; u++) {
      var uImg = usedImages[u];
      var label = uImg.is_hero ? ('🖼️ Hero-Hintergrund (' + uImg.filename + ')') : ('📷 ' + uImg.filename);
      btnsHtml += '<button type="button" class="btn-swap-target-choice" onclick="acpSelectTargetDirect(\'' + uImg.rel_path + '\', \'' + uImg.slot + '\', ' + uImg.is_hero + ', \'' + activeFile + '\')">' + label + '</button>';
    }
    btnsHtml += '<span style="color:#94a3b8; font-size:11px;">(oder klicke in der Vorschau darauf)</span></div>';
    targetHint.innerHTML = btnsHtml;
  } else {
    targetHint.innerHTML = '<span style="color:#facc15; font-size:12px; font-weight:700;">👉 Klicke jetzt in der Vorschau auf das Bild, das du ersetzen möchtest...</span>';
  }
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

  acpRenderSwapDockTargets();

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

function acpSelectTargetDirect(srcPath, slotName, isHero, docFile, slotContext) {
  acpHandleSlotClick({
    slot: slotName,
    isImg: true,
    isHero: isHero,
    currentSrc: srcPath,
    datei: docFile,
    context: slotContext || ""
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
  acpClickedTargetElement = null;
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
  var currentSrc = (data.currentSrc || data.src || '').replace(/['"]/g, '').split('?')[0].trim();
  if (!currentSrc && data.isHero) {
    currentSrc = 'images/hero.jpg';
  }
  var cleanOld = currentSrc.split('/').pop().split('?')[0].trim();

  // 1. Primär: Explizit übergebene Datei
  var activeFile = data.datei || '';

  // 2. Sekundär: Echte Datei aus dem iFrame-Location auslesen
  if (!activeFile) {
    try {
      var frame = document.getElementById("acp-widget-viewport");
      if (frame && frame.contentDocument && frame.contentDocument.location) {
        var realFile = frame.contentDocument.location.pathname.split('/').pop().split('?')[0];
        if (realFile && realFile.endsWith('.html')) {
          activeFile = realFile;
        }
      }
    } catch(e) {}
  }

  // 3. Tertiär: Smart Resolver aus ACP_BILDER (weiss exakt, wo welches Foto vorkommt!)
  if (Array.isArray(ACP_BILDER) && cleanOld) {
    for (var b = 0; b < ACP_BILDER.length; b++) {
      if (ACP_BILDER[b].filename === cleanOld || ACP_BILDER[b].rel_path === currentSrc) {
        if (Array.isArray(ACP_BILDER[b].used_in) && ACP_BILDER[b].used_in.length > 0) {
          var inActive = ACP_BILDER[b].used_in.some(function(u) { return u.datei === activeFile; });
          if (!inActive) {
            activeFile = ACP_BILDER[b].used_in[0].datei;
          }
        }
        break;
      }
    }
  }

  // 4. Fallback auf aktiven Job
  if (!activeFile) {
    activeFile = (currentJob && currentJob.datei) || 'index.html';
  }

  acpTargetSwapSlot = {
    slot: data.slot || 'hero.hintergrund.bild',
    isImg: data.isImg,
    isHero: data.isHero,
    currentSrc: currentSrc,
    datei: activeFile,
    context: data.context || ''
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

    // Direktes In-Memory DOM-Update im iFrame (wirkt sofort ohne Seiten-Reload!)
    try {
      var idoc = frame.contentDocument || (frame.contentWindow && frame.contentWindow.document);
      if (idoc) {
        if (acpClickedTargetElement) {
          if (acpClickedTargetElement.tagName === "IMG") {
            acpClickedTargetElement.src = effectivePreviewSrc;
          } else {
            acpClickedTargetElement.style.backgroundImage = 'url("' + effectivePreviewSrc + '")';
          }
          acpClickedTargetElement.style.outline = "4px solid #22c55e";
        } else {
          var imgs = idoc.querySelectorAll("img");
          for (var m = 0; m < imgs.length; m++) {
            var isrc = (imgs[m].getAttribute("src") || "").replace(/['"]/g, "").split("?")[0].trim();
            if (isrc === acpTargetSwapSlot.currentSrc || (cleanOld && isrc.indexOf(cleanOld) !== -1)) {
              imgs[m].src = effectivePreviewSrc;
              imgs[m].style.outline = "4px solid #22c55e";
              break;
            }
          }
        }
      }
    } catch(e) {}
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
var acpSyncPollTimer = null;

function acpAutoSyncViewport(targetFile, cleanNewImageName, jobId) {
  if (acpSyncPollTimer) {
    clearTimeout(acpSyncPollTimer);
    acpSyncPollTimer = null;
  }

  var frame = document.getElementById("acp-widget-viewport");
  if (!frame) return;

  var currentSrc = frame.getAttribute("src") || frame.src || "";
  if (!currentSrc) return;

  // Saubere Basis-URL ohne veraltete Cache-Buster oder Probes
  var cleanBase = currentSrc.split("&t=")[0].split("?t=")[0].split("&_probe=")[0].split("?_probe=")[0];
  var sep = cleanBase.indexOf("?") === -1 ? "?" : "&";

  var pollCount = 0;
  var maxPolls = 14; // Bis zu 14 Versuche * 2000ms = 28 Sekunden
  var pollInterval = 2000;

  acpLog("info", "🔄 Starte automatische Edge-CDN-Synchronisation...", "Datei: " + targetFile + " · Neues Foto: " + cleanNewImageName);

  function pollEdge() {
    pollCount++;
    var probeUrl = cleanBase + sep + "_probe=" + Date.now();

    fetch(probeUrl, { cache: "no-store" })
      .then(function(res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.text();
      })
      .then(function(html) {
        var isLive = (cleanNewImageName && html.indexOf(cleanNewImageName) !== -1);
        if (isLive || pollCount >= maxPolls) {
          acpLog("success", "🎉 Edge CDN synchronisiert! Lade Viewport automatisch neu...", "Versuch " + pollCount + " · Datei: " + targetFile);
          acpReloadViewportWithTransition(cleanBase);
        } else {
          acpSyncPollTimer = setTimeout(pollEdge, pollInterval);
        }
      })
      .catch(function(err) {
        if (pollCount >= maxPolls) {
          acpLog("warn", "⚠️ Edge-Probe Timeout erreicht. Führe Fallback-Reload durch.");
          acpReloadViewportWithTransition(cleanBase);
        } else {
          acpSyncPollTimer = setTimeout(pollEdge, pollInterval);
        }
      });
  }

  // Erster CDN-Check nach 2.5 Sekunden
  acpSyncPollTimer = setTimeout(pollEdge, 2500);
}

function acpReloadViewportWithTransition(cleanBaseUrl) {
  var frame = document.getElementById("acp-widget-viewport");
  if (!frame) return;

  frame.style.transition = "opacity 0.25s ease";
  frame.style.opacity = "0.3";

  var sep = cleanBaseUrl.indexOf("?") === -1 ? "?" : "&";
  var reloadSrc = cleanBaseUrl + sep + "t=" + Date.now();

  frame.src = reloadSrc;
  frame.onload = function() {
    frame.style.opacity = "1";
    acpShowToast('🎉 <strong>Live-Vorschau aktualisiert!</strong><br><small>Die Seite wurde automatisch mit dem neuen Bild synchronisiert.</small>', 5000);
    acpLog("success", "✨ Vorschau automatisch aktualisiert", reloadSrc);
  };
}

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
  var cleanOld = (acpTargetSwapSlot.currentSrc.split('/').pop() || acpTargetSwapSlot.slot).split('?')[0].trim();
  var cleanNew = (acpSelectedSwapImage.filename || '').split('?')[0].trim();
  acpLog("swap", "🎯 Tauschziel im Inserat gewählt: " + cleanOld + " ➔ " + cleanNew, "Datei: " + activeFile + " · Slot: " + acpTargetSwapSlot.slot);

  acpShowToast('⚡ <strong>Bildtausch gestartet:</strong> Tausche ' + cleanOld + ' ➔ ' + cleanNew + '...<br><small>Cloudflare Pages aktualisiert den Edge-Cache...</small>', 8000);

  var payload = {
    client: (currentJob && currentJob.folder) || (window.ACP_CLIENT_PROFILE && window.ACP_CLIENT_PROFILE.slug) || 'preview-birchmeier',
    file: activeFile,
    old_path: acpTargetSwapSlot.currentSrc.split('?')[0].trim(),
    new_path: acpSelectedSwapImage.rel_path.split('?')[0].trim(),
    is_hero: !!acpTargetSwapSlot.isHero,
    slot: acpTargetSwapSlot.slot || "",
    context: acpTargetSwapSlot.context || ""
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
      // 1. Bild im iFrame-DOM sicher arretieren (Zero-Latency ohne 404-Bruch)
      var safePreviewSrc = (acpLocalBlobPreviews && (acpLocalBlobPreviews[payload.new_path] || acpLocalBlobPreviews[cleanNew])) || "";

      try {
        var f = document.getElementById("acp-widget-viewport");
        var idoc = f ? (f.contentDocument || (f.contentWindow && f.contentWindow.document)) : null;
        if (idoc) {
          var targetEl = acpClickedTargetElement;
          if (!targetEl) {
            var allImgs = idoc.querySelectorAll("img");
            for (var k = 0; k < allImgs.length; k++) {
              var imgS = (allImgs[k].getAttribute("src") || "").replace(/['"]/g, "").split("?")[0].trim();
              if (imgS === payload.old_path || (cleanOld && imgS.indexOf(cleanOld) !== -1)) {
                targetEl = allImgs[k];
                break;
              }
            }
          }
          if (targetEl) {
            if (safePreviewSrc && (safePreviewSrc.startsWith("blob:") || safePreviewSrc.startsWith("data:"))) {
              if (targetEl.tagName === "IMG") {
                targetEl.src = safePreviewSrc;
              } else {
                targetEl.style.backgroundImage = 'url("' + safePreviewSrc + '")';
              }
            } else {
              var probe = new Image();
              probe.onload = function() {
                if (targetEl.tagName === "IMG") {
                  targetEl.src = probe.src;
                } else {
                  targetEl.style.backgroundImage = 'url("' + probe.src + '")';
                }
              };
              probe.src = payload.new_path + "?t=" + Date.now();
            }
            targetEl.style.outline = "4px solid #22c55e";
            setTimeout((function(el) { return function() { if (el) el.style.outline = ""; }; })(targetEl), 4000);
          }
        }
      } catch(e) {}

      // 2. Swap-Dock & Spotlight lautlos schliessen
      acpCancelSwap(true);

      // 3. Bilder-Pool aktualisieren (zeigt nun an, wo das Bild neu im Einsatz ist)
      acpRefreshImages();

      // 4. Erfolgs-Meldung & Status
      acpLog("success", "🎉 Bildtausch auf dem Server verarbeitet!", "Edge CDN synchronisiert · Datei: " + payload.file);
      acpShowToast('⚡ <strong>Bild im HTML verankert!</strong><br><small>Edge CDN synchronisiert... Die Vorschau aktualisiert sich gleich automatisch.</small>', 15000);

      // 5. Automatischer Viewport Edge-CDN AutoSync & Seamless Reload!
      acpAutoSyncViewport(activeFile, cleanNew, (currentJob ? currentJob.id : null));
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
  var countDraft = countAll - countLive;

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
    var isWebsite = (typeof ACP_CLIENT_PROFILE !== "undefined" && (ACP_CLIENT_PROFILE.is_website_studio || (ACP_CLIENT_PROFILE.studio_title && ACP_CLIENT_PROFILE.studio_title.indexOf("WEBPILOT") !== -1)));
    var allLabel = isWebsite ? "📄 Alle Seiten" : "🏢 Alle Inserate";
    var liveLabel = isWebsite ? "🟢 Live publiziert" : "🟢 Live eingebettet";
    var pillsHtml = '<button type="button" class="acp-job-filter-pill' + (acpCurrentJobFilter === 'alle' ? ' active' : '') + '" data-filter="alle" onclick="acpSetJobFilter(\'alle\')">' + allLabel + ' (<span id="count-jobs-all">' + countAll + '</span>)</button>';
    
    pillsHtml += ' <button type="button" class="acp-job-filter-pill' + (acpCurrentJobFilter === 'live' ? ' active' : '') + '" data-filter="live" onclick="acpSetJobFilter(\'live\')">' + liveLabel + ' (<span id="count-jobs-live">' + countLive + '</span>)</button>';
    
    pillsHtml += ' <button type="button" class="acp-job-filter-pill' + (acpCurrentJobFilter === 'draft' ? ' active' : '') + '" data-filter="draft" onclick="acpSetJobFilter(\'draft\')">🟡 Entwürfe (<span id="count-jobs-draft">' + countDraft + '</span>)</button>';

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
    
    pillsContainer.innerHTML = pillsHtml;
  }

  var filtered = ACP_STELLEN.filter(function(j) {
    if (acpCurrentJobFilter === 'live' && !j.is_live) return false;
    if (acpCurrentJobFilter === 'draft' && j.is_live) return false;
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
    var emptyMsg = "Keine passenden Stellen gefunden.";
    if (acpCurrentJobFilter === "live") {
      emptyMsg = "Noch keine Stellen als Live-Widget eingebaut. Kopiere den Widget-Code eines Entwurfs, um ihn in deine Website einzubinden.";
    } else if (acpCurrentJobFilter === "draft") {
      emptyMsg = "Keine un-eingebetteten Entwürfe vorhanden. Alle Stellen sind aktuell live eingebunden.";
    }
    tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:48px 20px; color:#64748b; font-family:\'JetBrains Mono\',monospace; font-size:13px;">' + emptyMsg + '</td></tr>';
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
      var liveTgtUrl = j.embedded_page_url || j.live_url;
      var liveTgtLbl = j.embedded_page_label || (liveTgtUrl ? acpCleanUrlLabel(liveTgtUrl) : 'Live');
      statusBadge = '<div class="job-status-cell">' +
        '<a href="' + liveTgtUrl + '" target="_blank" rel="noopener noreferrer" class="acp-table-badge badge-live" title="Öffentlich eingebaut auf ' + liveTgtUrl + ' (Klicken, um die Live-Seite im neuen Tab zu öffnen)">' +
          '<span class="badge-dot-live">●</span> LIVE WIDGET ↗' +
        '</a>' +
        '<div class="job-embedded-subline" title="' + liveTgtUrl + '">Eingebaut: <strong>' + liveTgtLbl + '</strong></div>' +
      '</div>';
    } else if (j.id && j.id.indexOf("zurbuchen") !== -1) {
      statusBadge = '<div class="job-status-cell">' +
        '<span class="acp-table-badge badge-ready">' +
          '<span class="badge-dot-ready">●</span> BEREIT' +
        '</span>' +
        '<div class="job-embedded-subline text-muted">Bereit zur Einbettung</div>' +
      '</div>';
    } else {
      statusBadge = '<div class="job-status-cell">' +
        '<span class="acp-table-badge badge-draft">' +
          '<span class="badge-dot-draft">●</span> ENTWURF' +
        '</span>' +
        '<div class="job-embedded-subline text-muted">Nicht eingebaut</div>' +
      '</div>';
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
  var studioTitle = (typeof ACP_CLIENT_PROFILE !== "undefined" && ACP_CLIENT_PROFILE.studio_title) ? ACP_CLIENT_PROFILE.studio_title : "WEBPILOT STUDIO";
  var isWebsiteStudio = (studioTitle.indexOf("WEBPILOT") !== -1 || (typeof ACP_CLIENT_PROFILE !== "undefined" && ACP_CLIENT_PROFILE.is_website_studio));

  if (badgeLabel) badgeLabel.textContent = studioTitle;
  if (brandBadge) brandBadge.title = studioTitle + (isOnline ? " (Online auf Cloudflare Pages)" : " (Lokal)");

  if (isWebsiteStudio) {
    var pickerHeader = document.querySelector(".acp-dropdown-header span:first-child");
    if (pickerHeader) pickerHeader.innerHTML = 'Seite auswählen (<span id="dropdown-count">' + ACP_STELLEN.length + '</span>)';
    var navDir = document.querySelector(".acp-nav-btn-directory .nav-label");
    if (navDir) navDir.textContent = "Seiten";
    var navDirBtn = document.querySelector(".acp-nav-btn-directory");
    if (navDirBtn) navDirBtn.title = "Seiten-Zentrale: Navigation & Entwürfe";
  }

  if (isOnline) {
    if (onlineBtn) {
      onlineBtn.innerHTML = '<span class="nav-icon">🔗</span><span class="nav-label">Link</span>';
      onlineBtn.title = "Link zu diesem Online-Cockpit in die Zwischenablage kopieren";
      onlineBtn.onclick = function(e) {
        e.preventDefault();
        acpCopyOnlineUrl(onlineBtn);
      };
    }
  } else {
    if (onlineBtn) {
      var fallbackUrl = (typeof ACP_CLIENT_PROFILE !== "undefined" && ACP_CLIENT_PROFILE.host_url) ? ACP_CLIENT_PROFILE.host_url : window.location.href;
      onlineBtn.href = fallbackUrl;
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
// [SEKTIONEN & KI-COACH] INTERAKTIVE WEBPILOT COACH ENGINE
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

function acpGetSectionArchetype(sec) {
  var id = (sec.id || "").toLowerCase();
  var raw = (sec.raw || sec.outerHTML || "").toLowerCase();
  var kicker = (sec.kicker || "").toLowerCase();
  var title = (sec.title || "").toLowerCase();

  if (id === "top-bar" || id === "header" || sec.tag === "header") {
    return { name: "KOPFZEILE & NAV", icon: "🧭", color: "rgba(148, 163, 184, 0.18)", text: "#94a3b8" };
  }
  if (id === "footer" || sec.tag === "footer") {
    return { name: "FUSSZEILE & IMPRESSUM", icon: "⚖️", color: "rgba(148, 163, 184, 0.18)", text: "#94a3b8" };
  }
  if (id.includes("hero") || raw.includes("hero-wrap") || raw.includes("progress-hero")) {
    return { name: "HERO-BÜHNE", icon: "🖼️", color: "rgba(245, 158, 11, 0.2)", text: "#fbbf24" };
  }
  if (id.includes("stell") || id.includes("job") || raw.includes("job-card") || title.includes("position") || title.includes("fachbereich")) {
    return { name: "OFFENE STELLEN", icon: "💼", color: "rgba(59, 130, 246, 0.2)", text: "#60a5fa" };
  }
  if (id.includes("vorteil") || id.includes("benefit") || id.includes("kultur") || title.includes("mehrwert") || title.includes("warum")) {
    return { name: "VORTEILE & KULTUR", icon: "⭐", color: "rgba(234, 179, 8, 0.2)", text: "#facc15" };
  }
  if (id.includes("bewerb") || id.includes("apply") || raw.includes("apply-section") || title.includes("bewerbung")) {
    return { name: "EXPRESS-BEWERBUNG", icon: "📱", color: "rgba(16, 185, 129, 0.2)", text: "#34d399" };
  }
  if (id.includes("team") || raw.includes("team-card") || title.includes("team") || title.includes("meister")) {
    return { name: "TEAM & BETRIEB", icon: "👥", color: "rgba(168, 85, 247, 0.2)", text: "#c084fc" };
  }
  if (id.includes("kontakt") || raw.includes("contact") || title.includes("kontakt") || title.includes("pikett")) {
    return { name: "KONTAKT & 24H-PIKETT", icon: "📞", color: "rgba(239, 68, 68, 0.2)", text: "#f87171" };
  }
  return { name: "INHALTS-ABSCHNITT", icon: "📄", color: "rgba(245, 158, 11, 0.15)", text: "#fbbf24" };
}

function acpAnalyzeSectionContent(secEl) {
  var imgs = secEl.querySelectorAll("img, picture, svg");
  var allWithStyle = secEl.querySelectorAll("[style*='url('], [style*='background-image']");
  var totalImages = imgs.length + allWithStyle.length;

  var text = secEl.innerText || "";
  var wordCount = text.trim().split(/\s+/).filter(Boolean).length;

  var cards = secEl.querySelectorAll(".job-card, .benefit-card, .team-card, .feature-card, .step-item");
  var cardCount = cards.length;

  return {
    images: totalImages,
    words: wordCount,
    cards: cardCount
  };
}

function acpGenerateMiniPreviewSrcdoc(secHtml) {
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  var stylesHtml = "";
  var baseHref = "";

  if (doc) {
    baseHref = doc.location.href;
    var linksAndStyles = doc.querySelectorAll("link[rel='stylesheet'], style, link[rel='preconnect']");
    linksAndStyles.forEach(function(el) {
      stylesHtml += el.outerHTML + "\n";
    });
  }

  return '<!DOCTYPE html><html><head>' +
    '<base href="' + baseHref + '">' +
    '<meta charset="utf-8">' +
    '<meta name="viewport" content="width=1200">' +
    stylesHtml +
    '<style>' +
    '  html, body { margin:0; padding:0; background: #06090e !important; overflow: hidden !important; width:1200px !important; min-height: 600px !important; }' +
    '  .section-wrap, .hero-wrap, .apply-section, header, footer { animation: none !important; opacity: 1 !important; transform: none !important; }' +
    '  * { -webkit-font-smoothing: antialiased; }' +
    '</style>' +
    '</head><body>' +
    secHtml +
    '</body></html>';
}

function acpScrollToSectionInViewport(secId) {
  console.log("[WebPilot Studio] 🎯 Springe zu Sektion:", secId);
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) {
    console.warn("[WebPilot Studio] Kein iframe-Document gefunden");
    return;
  }

  // 1. Suche nach data-section oder id
  var targetEl = doc.querySelector('[data-section="' + secId + '"]') || doc.getElementById(secId);

  // 2. Smarte Fallbacks nach Archetyp / Klassen
  if (!targetEl) {
    if (secId === "hero" || secId.includes("hero")) {
      targetEl = doc.querySelector(".hero-wrap, .page-hero, .hero, section");
    } else if (secId === "top-bar" || secId === "header") {
      targetEl = doc.querySelector("header, .top-bar, .header-wrap");
    } else if (secId === "footer") {
      targetEl = doc.querySelector("footer, .footer-wrap, .block-footer");
    } else if (secId === "leistungen" || secId.includes("service")) {
      targetEl = doc.querySelector("#leistungen, .service-cards, [id*='leistung']");
    } else if (secId === "stellen" || secId.includes("job")) {
      targetEl = doc.querySelector("#stellen, .jobs-grid, [id*='stell']");
    } else if (secId === "vorteile" || secId.includes("benefit")) {
      targetEl = doc.querySelector("#vorteile, .benefits-grid, [id*='vorteil']");
    } else if (secId === "bewerben" || secId.includes("apply")) {
      targetEl = doc.querySelector("#bewerben, .apply-section, form");
    }
  }

  if (!targetEl) {
    console.warn("[WebPilot Studio] Sektion nicht im DOM gefunden:", secId);
    return;
  }

  // Modal schliessen
  if (acpSectionsModalOpen) {
    acpToggleSectionsModal();
  }

  // Sanftes Scrollen zur Zielsektion
  try {
    targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
  } catch (e) {
    targetEl.scrollIntoView();
  }

  // Visueller bernsteinfarbener Hervorhebungs-Impuls (2.5 Sekunden)
  var origTransition = targetEl.style.transition;
  var origOutline = targetEl.style.outline;
  var origShadow = targetEl.style.boxShadow;

  targetEl.style.transition = 'all 0.3s ease';
  targetEl.style.outline = '3px solid #f59e0b';
  targetEl.style.boxShadow = '0 0 50px rgba(245, 158, 11, 0.5)';

  setTimeout(function() {
    targetEl.style.outline = origOutline;
    targetEl.style.boxShadow = origShadow;
    targetEl.style.transition = origTransition;
  }, 2500);
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
    var elements = doc.querySelectorAll("[data-section], section, header.site-header, footer.site-footer, header.top-bar, footer.footer-wrap, .header-wrap, .footer-wrap");
    elements.forEach(function(el, idx) {
      var id = el.getAttribute("data-section") || el.id;
      if (!id) {
        if (el.tagName.toLowerCase() === "header") id = "top-bar";
        else if (el.tagName.toLowerCase() === "footer") id = "footer";
        else if (el.className && (el.className.includes("hero") || el.className.includes("page-hero"))) id = "hero";
        else id = "section-" + (idx + 1);
      }
      // Garantiere data-section im Live-iFrame DOM für deterministisches Anspringen
      if (!el.getAttribute("data-section")) {
        el.setAttribute("data-section", id);
      }

      if (id === "acp-cockpit-bar" || el.closest(".acp-cockpit-bar")) return;
      if (acpScannedSections.some(function(s) { return s.id === id; })) return;

      var kicker = el.querySelector(".section-kicker, .hero-kicker, .kicker, .tag");
      var title = el.querySelector(".section-title, .hero-title, h1, h2, h3");

      var kickerText = kicker ? kicker.innerText.trim() : "";
      var titleText = title ? title.innerText.trim() : (el.getAttribute("aria-label") || id);

      var lines = el.outerHTML.split("\n").length;
      var charCount = el.outerHTML.length;
      var analysis = acpAnalyzeSectionContent(el);

      acpScannedSections.push({
        id: id,
        tag: el.tagName.toLowerCase(),
        kicker: kickerText,
        title: titleText,
        lines: lines,
        chars: charCount,
        outerHTML: el.outerHTML,
        analysis: analysis,
        index: idx
      });
    });
  }

  if (badge) {
    badge.textContent = "● " + acpScannedSections.length + " Sektionen aktiv";
  }

  grid.innerHTML = "";
  acpScannedSections.forEach(function(sec, idx) {
    var card = document.createElement("div");
    card.className = "acp-section-card";

    var isSystem = (sec.id === "header" || sec.id === "footer" || sec.id === "top-bar");
    var archetype = acpGetSectionArchetype(sec);
    var srcdocHtml = acpGenerateMiniPreviewSrcdoc(sec.outerHTML);

    var metaTagsHtml = "";
    if (sec.analysis) {
      if (sec.analysis.images > 0) metaTagsHtml += '<span class="acp-sec-meta-tag">📷 ' + sec.analysis.images + ' ' + (sec.analysis.images === 1 ? 'Bild' : 'Bilder') + '</span> · ';
      if (sec.analysis.cards > 0) metaTagsHtml += '<span class="acp-sec-meta-tag">💼 ' + sec.analysis.cards + ' Kacheln</span> · ';
      metaTagsHtml += '<span class="acp-sec-meta-tag">📝 ca. ' + sec.analysis.words + ' Wörter</span>';
    }

    card.innerHTML = 
      '<div>' +
        '<div class="acp-sec-head" style="margin-bottom: 12px;">' +
          '<span class="acp-sec-archetype-pill" style="background:' + archetype.color + '; color:' + archetype.text + ';">' +
            archetype.icon + ' ' + archetype.name +
          '</span>' +
          '<span class="acp-sec-id-badge">data-section="' + sec.id + '"</span>' +
        '</div>' +

        '<div class="acp-sec-mini-stage" onclick="acpScrollToSectionInViewport(\'' + sec.id + '\')" title="Klicken, um im Live-Simulator direkt zu diesem Abschnitt zu springen">' +
          '<iframe class="acp-sec-mini-iframe" srcdoc="' + srcdocHtml.replace(/"/g, '&quot;') + '"></iframe>' +
          '<div class="acp-sec-mini-overlay" onclick="acpScrollToSectionInViewport(\'' + sec.id + '\')">' +
            '<button type="button" class="acp-sec-mini-jump-btn" onclick="event.stopPropagation(); acpScrollToSectionInViewport(\'' + sec.id + '\')"><span>👁️ Im Simulator ansehen</span></button>' +
          '</div>' +
        '</div>' +

        '<div style="margin-top: 14px;">' +
          (sec.kicker ? '<div style="font-family:\'JetBrains Mono\',monospace; font-size:11px; color:#f59e0b; margin-bottom:4px; font-weight:700;">' + sec.kicker + '</div>' : '') +
          '<h4 style="color:#fff; font-size:15px; font-weight:700; line-height:1.4; margin: 0 0 8px 0;">' + sec.title + '</h4>' +
          '<div class="acp-sec-meta-row">' +
            metaTagsHtml +
          '</div>' +
        '</div>' +
      '</div>' +

      '<div style="display:flex; gap:8px; flex-wrap:wrap; padding-top:14px; border-top:1px solid rgba(255,255,255,0.08);">' +
        '<button type="button" class="acp-btn-secondary" onclick="acpCopySectionPrompt(\'' + sec.id + '\')" style="flex:1.2; padding:9px 12px; font-size:12.5px; justify-content:center; background:rgba(245,158,11,0.12); border-color:rgba(245,158,11,0.3); color:#fbbf24; font-weight:700;" title="Kopiert den interaktiven Coach-Prompt für ChatGPT oder Claude">' +
          '<span>💬 KI-Coach konsultieren</span>' +
        '</button>' +
        '<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal(\'' + sec.id + '\')" style="padding:9px 12px; font-size:12.5px; font-weight:700; color:#34d399; background:rgba(16,185,129,0.12); border-color:rgba(16,185,129,0.35);" title="Neuen Text oder KI-Code einfügen & dauerhaft speichern">' +
          '<span>✏️ Text / Code einfügen</span>' +
        '</button>' +
        '<button type="button" class="acp-btn-secondary" onclick="acpScrollToSectionInViewport(\'' + sec.id + '\')" style="padding:9px 10px; font-size:12.5px;" title="Im Simulator ansehen">' +
          '<span>👁️</span>' +
        '</button>' +
      '</div>';

    grid.appendChild(card);
  });
}

function acpBuildSectionCoachPrompt(targetSecId) {
  var targetSec = acpScannedSections.find(function(s) { return s.id === targetSecId; });
  if (!targetSec) return "";

  var sectionsOutline = acpScannedSections.map(function(s, i) {
    return "   " + (i + 1) + ". [" + s.id + "] " + (s.kicker ? s.kicker + " · " : "") + s.title;
  }).join("\n");

  var targetIdx = acpScannedSections.findIndex(function(s) { return s.id === targetSecId; });
  var prevSec = targetIdx > 0 ? acpScannedSections[targetIdx - 1] : null;
  var nextSec = targetIdx < acpScannedSections.length - 1 ? acpScannedSections[targetIdx + 1] : null;

  var prevInfo = prevSec ? "Direkt davor liegt: [" + prevSec.id + "] " + prevSec.title : "Liegt ganz oben auf der Seite (Hero-Bühne)";
  var nextInfo = nextSec ? "Direkt danach folgt: [" + nextSec.id + "] " + nextSec.title : "Schliesst die Seite ab (direkt vor dem Footer)";

  var profile = window.ACP_CLIENT_PROFILE || {};
  var companyName = profile.company_name || profile.name || "unser Betrieb";
  var industryLabel = profile.industry_label || "Schweizer Handwerks- & Meisterbetrieb";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Handwerker EFZ / Fachmonteure\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\"), \"24h-Pikett\" (nie \"Notdienst\").";

  var prompt = 
"================================================================================\n" +
"🚨 STRIKTE VERHALTENSREGEL FÜR DEINE ALLERERSTE ANTWORT:\n" +
"GIB JETZT NOCH KEINEN PROGRAMMIERCODE AUS! KEIN HTML, KEIN CSS, KEIN JAVASCRIPT!\n" +
"================================================================================\n\n" +

"Du bist mein persönlicher WebPilot Sektions-Coach für " + companyName + " (" + industryLabel + ").\n" +
"Ich übergebe dir hier den aktuellen Stand unserer Webseiten-Sektion \"" + targetSec.title + "\" (data-section=\"" + targetSec.id + "\").\n\n" +

"DEINE AUFGABE IN DIESEM CHAT:\n" +
"Coache mich als Inhaber / Webseiten-Betreiber sympathisch, lösungsorientiert und strukturiert durch die Optimierung dieses Abschnitts. Führe ein aktives Beratungsgespräch mit mir, statt mich mit Code zu überrollen!\n\n" +

"--------------------------------------------------------------------------------\n" +
"ANTWORTE IN DEINEM ALLERERSTEN SCHRITT EXAKT IN DIESEM 4-PUNKTE-FORMAT:\n" +
"--------------------------------------------------------------------------------\n" +
"1. Freundliche Begrüssung: Begrüsse mich kurz und stelle dich als mein persönlicher WebPilot-Coach für die Sektion \"" + targetSec.title + "\" vor.\n" +
"2. Ehrlicher Status-Check: Fasse in 2 bis 3 Sätzen zusammen, wie dieser Abschnitt aktuell auf Schweizer Besucher und Fachkräfte wirkt und wo er noch Potenzial hat.\n" +
"3. 3 bis 4 konkrete Coaching-Impulse: Mache mir 3-4 massgeschneiderte, sofort verständliche Vorschläge für diesen Abschnitt (z.B. A: Nutzenversprechen schärfen, B: Neues Team- oder Leistungselement hinzufügen, C: Tonalität & Vertrauensbeweise stärken, D: Spezifischer Wunsch nach meiner Wahl).\n" +
"4. Die Coach-Frage: Frage mich am Ende direkt: «Welche dieser Richtungen spricht Sie am meisten an, oder was möchten Sie ganz konkret verändern?»\n\n" +

"--------------------------------------------------------------------------------\n" +
"REGEL FÜR DEN SPÄTEREN CODE-EXPORT (ERST NACH FREIGABE IM CHAT):\n" +
"--------------------------------------------------------------------------------\n" +
"Erst wenn wir die Änderungen gemeinsam besprochen haben und ich sage «Ja, bitte den Code ausgeben» oder «Erstelle den HTML-Code», gibst du mir den vollständigen, sauberen HTML-Codeblock von <section ...> bis </section> aus.\n" +
"- 100% syntaktisch sauber: Alle Tags (<section>, <div>, <span>, <p>) vollständig geschlossen.\n" +
"- Keine Code-Auslassungen (keine Platzhalter wie '... restlicher Code ...')!\n" +
"- Keine <script> oder <iframe> Tags in der Sektion.\n\n" +

"================================================================================\n" +
"GESAMT-KONTEXT DER SEITE (FÜR TONALITÄT, ROTEN FADEN & DESIGN-FLOW):\n" +
"================================================================================\n" +
"- Alle Abschnitte dieser Seite im Überblick:\n" + sectionsOutline + "\n\n" +
"- Position dieser Sektion im Fluss der Seite:\n" +
"  * " + prevInfo + "\n" +
"  * " + nextInfo + "\n\n" +

"================================================================================\n" +
"VERBINDLICHE SCHWEIZER SPRACH- & DESIGN-DOKTRIN:\n" +
"================================================================================\n" +
"- Sprache: Authentisches Schweizer Hochdeutsch (100% Verbot von \"ß\", verwende immer \"ss\").\n" +
promptRules + "\n" +
"- Schweizer Typografie: Nutze die Klassen (.section-wrap, .section-inner, .section-kicker, .section-title, .section-desc).\n" +
"- Kicker-Regel: <span class=\"section-kicker\">● Kicker-Text</span> ist 100% freistehend in JetBrains Mono (niemals in einer Box oder einem Badge-Rahmen).\n" +
"- Fluchtlinie: max-width 1100px mit margin 0 auto.\n" +
"- Bilder: Relative Pfade wie \"images/[dateiname.jpg]\".\n\n" +

"================================================================================\n" +
"AKTUELLER QUELLTEXT DIESER SEKTION (ZUR ANALYSE):\n" +
"================================================================================\n" +
targetSec.outerHTML;

  return prompt;
}

function acpCopySectionPrompt(secId) {
  var promptText = acpBuildSectionCoachPrompt(secId);
  if (!promptText) return;

  navigator.clipboard.writeText(promptText).then(function() {
    acpShowCoachPromptSuccessModal(secId);
  }).catch(function() {
    window.prompt("Kopiere diesen Prompt für ChatGPT / Claude:", promptText);
  });
}

function acpShowCoachPromptSuccessModal(secId) {
  var targetSec = acpScannedSections.find(function(s) { return s.id === secId; });
  var title = targetSec ? targetSec.title : secId;

  var oldToast = document.getElementById("acp-coach-copied-toast");
  if (oldToast && oldToast.parentNode) oldToast.parentNode.removeChild(oldToast);

  var toast = document.createElement("div");
  toast.id = "acp-coach-copied-toast";
  toast.className = "acp-coach-toast";

  toast.innerHTML = 
    '<div style="display:flex; justify-content:space-between; align-items:flex-start;">' +
      '<div style="display:flex; align-items:center; gap:10px;">' +
        '<span style="font-size:24px;">💬</span>' +
        '<div>' +
          '<div style="font-family:\'JetBrains Mono\',monospace; font-size:11px; color:#f59e0b; font-weight:700;">// KI-COACH PROMPT KOPIERT</div>' +
          '<div style="font-size:14px; font-weight:700; color:#fff;">Sektion «' + title + '»</div>' +
        '</div>' +
      '</div>' +
      '<button type="button" onclick="this.closest(\'.acp-coach-toast\').remove()" style="background:none; border:none; color:#64748b; font-size:16px; cursor:pointer; padding:0 4px;">✕</button>' +
    '</div>' +
    '<p style="font-size:12.5px; color:#94a3b8; margin:0; line-height:1.45;">' +
      'Der Coach-Prompt wurde in deine Zwischenablage kopiert. Öffne jetzt einfach deine bevorzugte KI und füge ihn mit <strong>Strg + V</strong> ein:' +
    '</p>' +
    '<div style="display:flex; gap:10px; margin-top:8px; flex-wrap:wrap;">' +
      '<a href="https://chatgpt.com/" target="_blank" rel="noopener" style="flex:1; min-width:130px; text-align:center; background:#10a37f; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🤖 ChatGPT öffnen ↗</span>' +
      '</a>' +
      '<a href="https://claude.ai/" target="_blank" rel="noopener" style="flex:1; min-width:130px; text-align:center; background:#d97706; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🧠 Claude öffnen ↗</span>' +
      '</a>' +
      '<button type="button" onclick="this.closest(\'.acp-coach-toast\').remove(); acpOpenReplaceSectionModal(\'' + secId + '\')" style="flex:1.4; min-width:160px; text-align:center; background:linear-gradient(135deg, #10b981 0%, #059669 100%); color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; border:none; cursor:pointer; display:inline-flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 2px 8px rgba(16,185,129,0.3);">' +
        '<span>✏️ Antwort hier einfügen →</span>' +
      '</button>' +
    '</div>';

  document.body.appendChild(toast);

  setTimeout(function() {
    if (toast && toast.parentNode) {
      toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(20px)';
      setTimeout(function() { if (toast && toast.parentNode) toast.parentNode.removeChild(toast); }, 400);
    }
  }, 10000);
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
  var companyName = profile.company_name || profile.name || "unser Betrieb";
  var industryLabel = profile.industry_label || "Schweizer Unternehmens-Website";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Handwerker EFZ / Fachmonteure\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\").";

  var prompt = 
"Du bist mein technischer Web-Redakteur für " + companyName + " (" + industryLabel + ").\n" +
"Ich übergebe dir hier den VOLLSTÄNDIGEN Quellcode meiner Website (HTML5).\n\n" +
"MEINE REGELN:\n" +
"1. Schweizer Hochdeutsch (0x scharfes S, nur 'ss', Schweizer Fachbegriffe):\n" +
promptRules + "\n" +
"2. Schweizer Obsidian-Design & bestehende Klassen beibehalten.\n" +
"3. AUSGABE-PFLICHT: Gib mir den Quellcode immer als eine einzige, vollständige und ungekürzte HTML-Datei aus – ausnahmslos von <!DOCTYPE html> bis </html>. Verwende keine Code-Auslassungen!\n\n" +
"QUELLCODE:\n" + fullHtml;

  navigator.clipboard.writeText(prompt).then(function() {
    alert("✓ Komplette HTML-Seite inklusive Master-Prompt kopiert!\n\nJetzt in ChatGPT oder Claude einfügen.");
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
  var feedback = document.getElementById("acp-replace-live-feedback");
  var counter = document.getElementById("acp-replace-char-counter");

  if (title) {
    var targetSec = (acpScannedSections || []).find(function(s) { return s.id === secId; });
    var secTitle = targetSec && targetSec.title ? (' «' + targetSec.title + '»') : '';
    title.textContent = "Sektion [" + secId + "]" + secTitle + " — Neuer Text / Code";
  }
  if (textarea) {
    textarea.value = "";
    textarea.placeholder = "Hier die Antwort oder den neuen Text von ChatGPT / Claude für Sektion [" + secId + "] einfügen (Strg + V)...";
  }
  if (status) {
    status.style.display = "none";
    status.innerHTML = "";
  }
  if (counter) {
    counter.textContent = "0 Zeichen";
  }
  if (feedback) {
    feedback.innerHTML = '<span style="color:#94a3b8;">⚪ Noch kein Inhalt eingefügt. Füge deinen Text mit Strg + V ein.</span>';
  }

  if (modal) {
    modal.classList.add("is-open");
    modal.style.display = "flex";
  }
  acpUpdateBodyModalClass();

  // Fokus sofort ins Eingabefeld
  setTimeout(function() {
    if (textarea) textarea.focus();
  }, 100);
}

function acpCloseReplaceSectionModal() {
  var modal = document.getElementById("acp-replace-section-modal");
  if (modal) {
    modal.classList.remove("is-open");
    modal.style.display = "none";
  }
  acpUpdateBodyModalClass();
}

function acpUpdateReplaceTextFeedback() {
  var textarea = document.getElementById("acp-replace-code-input");
  var feedback = document.getElementById("acp-replace-live-feedback");
  var counter = document.getElementById("acp-replace-char-counter");
  var status = document.getElementById("acp-replace-airbag-status");
  if (!textarea || !feedback) return;

  var val = textarea.value.trim();
  if (counter) {
    counter.textContent = val.length + " Zeichen";
  }

  if (!val) {
    feedback.innerHTML = '<span style="color:#94a3b8;">⚪ Noch kein Inhalt eingefügt. Füge deinen Text mit Strg + V ein.</span>';
    if (status) status.style.display = "none";
    return;
  }

  var lines = val.split("\n").length;
  var words = val.split(/\s+/).filter(Boolean).length;
  var chars = val.length;

  feedback.innerHTML = 
    '<span style="display:inline-flex; align-items:center; gap:8px; color:#10b981; font-weight:700;">' +
      '<span style="font-size:16px;">🟢</span>' +
      '<span>✓ Text ist drin! ' + lines + ' Zeilen • ' + words + ' Wörter • ' + chars + ' Zeichen erkannt. Bereit zum Absenden!</span>' +
    '</span>';
}

function acpNormalizeAndValidateSection(rawInput, secId) {
  if (!rawInput || !rawInput.trim()) {
    return { ok: false, error: "Das Textfeld ist noch leer. Bitte füge zuerst den Text oder Code ein." };
  }

  var clean = rawInput.trim();

  // 1. Markdown-Codefences entfernen (```html ... ``` oder ``` ... ```)
  if (clean.startsWith("```")) {
    clean = clean.replace(/^```[a-zA-Z]*\n?/, "");
    clean = clean.replace(/\n?```$/, "").trim();
  }

  // 2. Sicherheits-Check: Keine ausführbaren Skripte oder iframes
  var forbiddenTags = /<(script|iframe|object|embed|form|meta|base|style)\b[^>]*>/i;
  var mTag = clean.match(forbiddenTags);
  if (mTag) {
    return { ok: false, error: "Sicherheits-Schranke: Ausführbare Tags (<" + mTag[1] + ">) sind in Inhalts-Sektionen verboten." };
  }
  if (/\son[a-zA-Z]+\s*=/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: Inline-JavaScript (on... Event-Handler) ist verboten." };
  }
  if (/(href|src|action)\s*=\s*["'\s]*javascript:/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: javascript:... Links sind nicht erlaubt." };
  }

  // 3. Intelligente Sektions-Hülle (Wrapping):
  var isAlreadySection = /^<(section|header|footer)\b[^>]*>/i.test(clean) && /<\/(section|header|footer)>$/i.test(clean);

  if (!isAlreadySection) {
    // Wenn HTML-Tags enthalten sind:
    if (/<[a-z][\s\S]*>/i.test(clean)) {
      clean = '<section class="section-wrap" id="' + secId + '" data-section="' + secId + '">\n  <div class="section-inner">\n' + clean + '\n  </div>\n</section>';
    } else {
      // Reiner Text: Absätze in <p> wrappen
      var paragraphs = clean.split(/\n\s*\n/).map(function(p) {
        return '    <p class="section-desc">' + p.trim().replace(/\n/g, '<br>') + '</p>';
      }).join('\n');
      clean = '<section class="section-wrap" id="' + secId + '" data-section="' + secId + '">\n  <div class="section-inner">\n' + paragraphs + '\n  </div>\n</section>';
    }
  } else {
    // Sicherstellen, dass data-section gesetzt ist
    if (!clean.includes('data-section=')) {
      clean = clean.replace(/^<(section|header|footer)\b/i, '<$1 data-section="' + secId + '"');
    }
  }

  // 4. Tag-Balancierung
  var checkTags = ["section", "div", "p", "span", "a", "h1", "h2", "h3", "h4", "ul", "ol", "li"];
  for (var i = 0; i < checkTags.length; i++) {
    var tag = checkTags[i];
    var openRegex = new RegExp("<" + tag + "(\s+[^>]*)?>", "gi");
    var closeRegex = new RegExp("</" + tag + ">", "gi");
    var openCount = (clean.match(openRegex) || []).length;
    var closeCount = (clean.match(closeRegex) || []).length;
    if (openCount !== closeCount) {
      return { 
        ok: false, 
        error: "Tag-Fehler bei <" + tag + ">: Wurde " + openCount + "x geöffnet, aber " + closeCount + "x geschlossen. Bitte schliesse alle <" + tag + "> Tags sauber ab." 
      };
    }
  }

  return { ok: true, html: clean };
}

function acpSubmitReplaceSection() {
  var textarea = document.getElementById("acp-replace-code-input");
  var status = document.getElementById("acp-replace-airbag-status");
  var applyBtn = document.getElementById("acp-btn-apply-replace");
  if (!textarea || !textarea.value) {
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "⚠️ <strong>Bitte zuerst Text einfügen:</strong> Das Feld ist noch leer.";
    }
    return;
  }

  var validation = acpNormalizeAndValidateSection(textarea.value, acpActiveEditSectionId);
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
  var targetFile = "index.html";
  if (iframe && iframe.getAttribute("src")) {
    var srcVal = iframe.getAttribute("src").split("?")[0];
    if (srcVal.endsWith(".html")) {
      targetFile = srcVal.split("/").pop();
    }
  }

  var clientSlug = window.ACP_CURRENT_CLIENT || (window.location.pathname.split("/")[1] || "preview-birchmeier");

  if (applyBtn) {
    applyBtn.disabled = true;
    applyBtn.innerHTML = "<span>⏳ Speichere &amp; Edge CDN synchronisieren...</span>";
  }

  if (status) {
    status.style.display = "block";
    status.style.color = "#fbbf24";
    status.style.background = "rgba(245, 158, 11, 0.1)";
    status.style.padding = "10px 14px";
    status.style.borderRadius = "6px";
    status.style.border = "1px solid rgba(245, 158, 11, 0.3)";
    status.innerHTML = "⚡ <strong>Airbag grün:</strong> Sende neue Sektion an Cloudflare Edge CDN...";
  }

  var payload = {
    client: clientSlug,
    file: targetFile,
    section_id: acpActiveEditSectionId,
    content: validation.html
  };

  fetch("/api/publish-career/replace-section", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(function(res) {
    if (!res.ok) {
      return res.json().then(function(j) { throw new Error(j.error || ("HTTP " + res.status)); });
    }
    return res.json();
  })
  .then(function(data) {
    if (applyBtn) {
      applyBtn.disabled = false;
      applyBtn.innerHTML = "<span>🚀 Änderung jetzt absenden &amp; live speichern</span>";
    }
    acpCloseReplaceSectionModal();

    if (typeof acpAutoSyncViewport === "function") {
      acpAutoSyncViewport("Sektion [" + acpActiveEditSectionId + "] aktualisiert");
    } else if (iframe) {
      var curSrc = iframe.src.split("?")[0];
      iframe.src = curSrc + "?t=" + Date.now();
    }

    setTimeout(function() {
      acpScanAndRenderSections();
    }, 1500);

    alert("🎉 Sektion [" + acpActiveEditSectionId + "] erfolgreich dauerhaft gespeichert und auf Cloudflare Pages bereitgestellt!");
  })
  .catch(function(err) {
    console.error("Fehler beim Ersetzen der Sektion:", err);
    if (applyBtn) {
      applyBtn.disabled = false;
      applyBtn.innerHTML = "<span>🚀 Änderung jetzt absenden &amp; live speichern</span>";
    }
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "🚨 <strong>Server-Fehler:</strong> " + err.message;
    }
  });
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
  if (modal) { modal.classList.add("is-open"); modal.style.display = "flex"; }
  acpUpdateBodyModalClass();
}

function acpCloseNewSectionModal() {
  var modal = document.getElementById("acp-new-section-modal");
  if (modal) { modal.classList.remove("is-open"); modal.style.display = "none"; }
  acpUpdateBodyModalClass();
}

function acpCopyGeneratedNewSectionPrompt() {
  var select = document.getElementById("acp-new-sec-position");
  var topicInput = document.getElementById("acp-new-sec-topic");
  var pos = select ? select.value : "services";
  var topic = topicInput && topicInput.value ? topicInput.value : "Unsere Partnerbetriebe & Netzwerke";

  var afterSec = acpScannedSections.find(function(s) { return s.id === pos; }) || acpScannedSections[0];
  var slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

  var profile = window.ACP_CLIENT_PROFILE || {};
  var companyName = profile.company_name || profile.name || "unser Betrieb";
  var industryLabel = profile.industry_label || "Schweizer Unternehmens-Website";
  var promptRules = (profile.prompt_rules && profile.prompt_rules.length > 0)
    ? profile.prompt_rules.join("\n")
    : "- Schweizer Geschäftsbegriffe: \"Leistungen\" (nie \"Gewerke\"), \"Handwerker EFZ / Fachmonteure\" (nie \"Gesellen\"), \"Lernende\" (nie \"Azubis\"), \"Offerte\" (nie \"Kostenvoranschlag\"), \"Ferien\" (nie \"Urlaub\").";

  var prompt = 
"================================================================================\n" +
"🚨 STRIKTE VERHALTENSREGEL FÜR DEINE ALLERERSTE ANTWORT:\n" +
"GIB JETZT NOCH KEINEN PROGRAMMIERCODE AUS! KEIN HTML, KEIN CSS, KEIN JAVASCRIPT!\n" +
"================================================================================\n\n" +

"Du bist mein persönlicher WebPilot Sektions-Coach für " + companyName + " (" + industryLabel + ").\n" +
"Wir möchten auf unserer Website einen völlig NEUEN Abschnitt zum Thema \"" + topic + "\" erstellen.\n\n" +

"POSITIONIERUNG IM SEITENFLUSS:\n" +
"- Der neue Abschnitt wird direkt NACH der Sektion [" + afterSec.id + "] \"" + afterSec.title + "\" eingefügt.\n\n" +

"ANTWORTE IN DEINEM ALLERERSTEN SCHRITT EXAKT IN DIESEM FORMAT:\n" +
"1. Kurze Begrüssung & Coaching-Einschätzung zu diesem neuen Thema.\n" +
"2. Mache mir 2 bis 3 konkrete Strukturvorschläge, wie wir dieses Thema am besten aufbauen (z.B. 3 Kacheln mit Icons, Vorher/Nachher Vergleich oder kompakter Infoblock).\n" +
"3. Frage mich, welche Variante mir am besten zusagt.\n\n" +

"ERST NACH MEINER FREIGABE:\n" +
"Erst wenn ich dir Feedback gebe, generierst du den fertigen HTML-Code von <section class=\"section-wrap\" data-section=\"" + slug + "\" id=\"" + slug + "\"> bis </section>.\n" +
"- Schweizer Typografie: .section-wrap, .section-inner, freistehender .section-kicker, .section-title, .section-desc.\n" +
"- Sprache: Schweizer Hochdeutsch (Verbot von scharfem S, nur 'ss').\n" +
promptRules;

  navigator.clipboard.writeText(prompt).then(function() {
    alert("✓ Neuer Coach-Prompt für zusätzlichen Abschnitt kopiert!\n\nJetzt in ChatGPT oder Claude einfügen.");
  }).catch(function() {
    window.prompt("Kopiere diesen Prompt:", prompt);
  });
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
    alert("✓ Sektion [" + secId + "] im Simulator ausgeblendet!");
  }
}

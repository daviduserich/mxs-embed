# 📑 Stellen-Verzeichnis & Widget-Einbettungscodes

Automatisch generierte Übersicht aller aktiven Recruiting-Stellen und Einbettungscodes für Webmaster.

---

## 1. Übersicht der aktiven Stellen & Live-Status

| Stelle | Firma | Lokale Datei | Direkte Edge-Vorschau (Link zum Teilen) | Ziel-Webseite (Host) | Live-Status |
|---|---|---|---|---|---|
| **🏠 Dachdecker EFZ (80–100%)** | Hiltbrand Gebäudehüllen AG | `Hiltbrand_Dachdecker.html` | [https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker.html](https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker.html) | [dachdecker-berneroberland.ch](https://dachdecker-berneroberland.ch) | ⚪ Entwurf |
| **🏠 Dachdecker EFZ (Pragmatisch & WhatsApp)** | Hiltbrand Gebäudehüllen AG | `Hiltbrand_Dachdecker_Pragmatisch.html` | [https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker_Pragmatisch.html](https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker_Pragmatisch.html) | [dachdecker-berneroberland.ch](https://dachdecker-berneroberland.ch) | 🟢 **Live auf Webseite** |
| **🌲 Zimmermann EFZ (November)** | Zurbuchen Holzbau AG | `Zurbuchen_Holzbauer_November.html` | [https://embed.magnet-xs.ch/zurbuchen/Zurbuchen_Holzbauer_November.html](https://embed.magnet-xs.ch/zurbuchen/Zurbuchen_Holzbauer_November.html) | [zurbuchen-holzbau.ch](https://www.zurbuchen-holzbau.ch) | 🟡 Bereit |
| **🌲 Zimmermann EFZ** | Zurbuchen Holzbau AG | `zurbuchen_Holzbauer.html` | [https://embed.magnet-xs.ch/zurbuchen/zurbuchen_Holzbauer.html](https://embed.magnet-xs.ch/zurbuchen/zurbuchen_Holzbauer.html) | [zurbuchen-holzbau.ch](https://www.zurbuchen-holzbau.ch) | 🟡 Bereit |

---

## 2. Widget-Einbettungscodes (Für den Webmaster)

### 🏠 Dachdecker EFZ (80–100%) (Hiltbrand Gebäudehüllen AG)
```html
<iframe src="https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker.html?embed=true" style="width:100%; border:none; min-height:850px;" scrolling="no" id="acp-job-widget"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="acp-embed-resize"){var el=document.getElementById("acp-job-widget");if(el)el.style.height=e.data.height+"px";}});<\/script>
```

### 🏠 Dachdecker EFZ (Pragmatisch & WhatsApp) (Hiltbrand Gebäudehüllen AG)
```html
<iframe src="https://embed.magnet-xs.ch/hiltbrand/Hiltbrand_Dachdecker_Pragmatisch.html?embed=true" style="width:100%; border:none; min-height:850px;" scrolling="no" id="acp-job-widget"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="acp-embed-resize"){var el=document.getElementById("acp-job-widget");if(el)el.style.height=e.data.height+"px";}});<\/script>
```

### 🌲 Zimmermann EFZ (November) (Zurbuchen Holzbau AG)
```html
<iframe src="https://embed.magnet-xs.ch/zurbuchen/Zurbuchen_Holzbauer_November.html?embed=true" style="width:100%; border:none; min-height:850px;" scrolling="no" id="acp-job-widget"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="acp-embed-resize"){var el=document.getElementById("acp-job-widget");if(el)el.style.height=e.data.height+"px";}});<\/script>
```

### 🌲 Zimmermann EFZ (Zurbuchen Holzbau AG)
```html
<iframe src="https://embed.magnet-xs.ch/zurbuchen/zurbuchen_Holzbauer.html?embed=true" style="width:100%; border:none; min-height:850px;" scrolling="no" id="acp-job-widget"></iframe>
<script>window.addEventListener("message",function(e){if(e.data&&e.data.type==="acp-embed-resize"){var el=document.getElementById("acp-job-widget");if(el)el.style.height=e.data.height+"px";}});<\/script>
```

---

## 3. Wie funktioniert die Aktualisierung? (Die 4-Stufen-Kaskade)
1. **Dein Laptop (Lokal):** Datei im Ordner bearbeiten (z. B. via ChatGPT) und im Cockpit prüfen (Entwurf).
2. **Magnet-XS Cloud (Airbag):** Bei Klick auf `[ 🚀 Jetzt scharfstellen ]` prüft der Airbag die Syntax & Links.
3. **Magnet-XS Edge-CDN (`embed.magnet-xs.ch`):** Baut und verteilt die Datei weltweit in unter 15 Sekunden.
4. **Kunden-Webseite:** Der iFrame in WordPress (`dachdecker-berneroberland.ch/jobs/`) zeigt sofort die neue Version!

💡 *Wichtig:* Nur diejenige Datei, deren Widget-Code in WordPress eingebunden ist (aktuell: `Hiltbrand_Dachdecker_Pragmatisch.html`), ist öffentlich live!


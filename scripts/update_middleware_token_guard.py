#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

mw_path = Path("/home/brainuser/workspaces/mxs-embed/functions/_middleware.js")
content = mw_path.read_text(encoding="utf-8")

# 1. Update clientTokens in both places
cryptic_token = "bm_live_9k7p2x4m8"

# Replace birchmeier tokens
content = re.sub(
    r"'birchmeier':\s*\[[^\]]+\],",
    f"'birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', '{cryptic_token}'],",
    content
)
content = re.sub(
    r"'preview-birchmeier':\s*\[[^\]]+\],",
    f"'preview-birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', '{cryptic_token}'],",
    content
)

# 2. Add redirect to /webpilot/ when unauthorized for birchmeier
cockpit_block = """    if (isCockpit) {
      if (!hasValidToken && !hasValidCookie) {
        if (clientSlug === 'birchmeier' || rootSegment.includes('birchmeier')) {
          return Response.redirect('https://vorschau.magnet-xs.ch/webpilot/', 302);
        }
        return new Response('Zugriff geschützt. Bitte Cockpit mit gültigem Mandanten-Token öffnen.', {
          status: 403,
          headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      }
    }"""

content = re.sub(
    r"if \(isCockpit\) \{\s*if \(!hasValidToken && !hasValidCookie\) \{.*?return new Response\('Zugriff geschützt[^;]+;\s*\}\s*\}",
    cockpit_block,
    content,
    flags=re.DOTALL
)

preview_block = """    else if ((isVorschauHost || isPreview) && !isEmbed && !hasValidToken && !hasValidCookie && !isAsset && !isOnboarding) {
      if (clientSlug === 'birchmeier' || rootSegment.includes('birchmeier')) {
        return Response.redirect('https://vorschau.magnet-xs.ch/webpilot/', 302);
      }
      return new Response('Vorschau geschützt. Bitte über das Mandanten-Cockpit mit Token aufrufen.', {
        status: 403,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }"""

content = re.sub(
    r"else if \(\(isVorschauHost \|\| isPreview\) && !isEmbed && !hasValidToken && !hasValidCookie && !isAsset && !isOnboarding\) \{.*?return new Response\('Vorschau geschützt[^;]+;\s*\}",
    preview_block,
    content,
    flags=re.DOTALL
)

mw_path.write_text(content, encoding="utf-8")
print(f"Middleware updated with cryptic token: {cryptic_token} and /webpilot/ redirect.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator-First WebPilot Showcase für Wüest + Paneduro («Innere Stärke entwickeln»)
URL: https://www.innere-staerke.business/
Erzeugt deterministisch beide Varianten:
  1. Komplettversion: preview-innere-staerke/ (index.html, angebot.html, ueber-uns.html, referenzen.html, kontakt.html + before.json)
  2. Zeigeversion (Vorschau-Entwurf): preview-innere-staerke-v2/ (index.html, kontakt.html + before.json)

Strikte Einhaltung von:
  - #UI-01..#UI-14 (Barlow + Plus Jakarta Sans, 0 JetBrains Mono, 0 //, 100% Lucide SVGs, 0 Emojis, 2-Radien 4px/8px)
  - #UI-03 Kunden-Sprache (0 Hausbau- oder Entwickler-Fachbegriffe)
  - #LANG-01..#LANG-02 (100% Schweizer Rechtschreibung ss statt Eszett)
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-innere-staerke"
V2_DIR = BASE_DIR / "preview-innere-staerke-v2"
V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

# 1. Vollständige Redesign-Inventur (before.json – 0 Datenverlust)
BEFORE_INVENTORY = {
    "source_url": "https://www.innere-staerke.business/",
    "crawled_at": "2026-11-03",
    "company": {
        "brand_name": "Wüest + Paneduro · Innere Stärke entwickeln",
        "legal_name": "Nino Paneduro GmbH",
        "uid_mwst": "CHE-279.321.936 MWST",
        "register": "Handelsregister des Kantons Luzern",
        "managing_directors": [
            "Antonino (Nino) Paneduro, Vorsitzender der Geschäftsführung",
            "Christine Wüest Paneduro, Geschäftsführerin"
        ],
        "address": {
            "location_name": "Businesspark Sursee",
            "street": "Allee 1b",
            "zip": "6210",
            "city": "Sursee",
            "canton": "Luzern",
            "country": "Schweiz"
        },
        "contact": {
            "phone_primary": "+41 78 606 20 56",
            "phone_secondary": "+41 79 468 21 46",
            "email": "mail@innere-staerke.business",
            "linkedin": "https://www.linkedin.com/company/mentalfitnesscenter/",
            "facebook_group": "https://www.facebook.com/groups/mentalfitnesscenter/"
        },
        "credits": {
            "portrait_photography": "Uwe Klössing"
        },
        "design_tokens_original": {
            "fonts": ["Barlow", "Plus Jakarta Sans"],
            "colors": {
                "charcoal_dark": "#3a3a39",
                "amber_gold": "#f9b231",
                "crimson_accent": "#ae031d",
                "white": "#ffffff"
            }
        }
    },
    "founders": [
        {
            "name": "Christine Wüest",
            "role": "Geschäftsführerin · Expertin für Resilienz, Selbstführung & innere Stärke",
            "headline": "Christine Wüest verbindet Expertise mit Empathie und Klarheit mit Kompetenz.",
            "image": "images/portrait-christine-wueest.jpg",
            "header_image": "images/header-christine-wueest.jpg",
            "biography": [
                "Christine Wüest verbindet Expertise mit Empathie und Klarheit mit Kompetenz. Sie ist ausgewiesene Expertin für Resilienz und innere Stärke – ein Thema, das sie schon lange begleitet.",
                "Ihre erste Begegnung mit innerer Stärke und dem, was diese bewirken kann, hatte Christine Wüest während ihrer Tätigkeit als Flight-Attendant bei der Swissair: «Dort war ich mit vielen unterschiedlichen Lebensrealitäten konfrontiert und fasziniert davon, wie Menschen mit innerer und mentaler Stärke teils enorme Herausforderungen meisterten.»",
                "Ihr beruflicher Weg führte sie nach dem Studium der Betriebswirtschaft in die IT-Branche, für die sie mehr als 10 Jahre in leitenden Positionen und in der Geschäftsleitung tätig war. Es folgten weitere Jahre in einem renommierten medizinischen Labor als Leiterin «Zentrale Dienste und HR» sowie in der Geschäftsleitung.",
                "Neben fachlichen Themen wurde sie dort immer wieder mit Fragen konfrontiert, die sich auf Resilienz bezogen: Wie gehe ich mit Druck und Stress um? Wie führe ich mich selbst? Oder wie erreiche ich meine Ziele? Um ihre Expertise auf diesem Gebiet weiter auszubauen, absolvierte Christine Wüest unter anderem eine Ausbildung zum Dipl. Mental Coach.",
                "Christine Wüest steht ihren Klientinnen und Klienten als klarer und zuverlässiger Coach und Ratgeber zur Seite. Gemeinsam erarbeitet sie Methoden, die am besten zur jeweiligen Situation passen, damit Klientinnen und Klienten ihr Leben und ihre Zukunft selbstbestimmt, kraftvoll und souverän gestalten."
            ]
        },
        {
            "name": "Nino Paneduro",
            "role": "Vorsitzender der Geschäftsführung · Mentor & Ratgeber für mentale Stärke, Fokus & Leadership",
            "headline": "Nino Paneduro steht für Fokus, Konzentration, mentale Stärke und Klarheit.",
            "image": "images/portrait-nino-paneduro.jpg",
            "header_image": "images/header-nino-paneduro.jpg",
            "biography": [
                "Nino Paneduro steht für Fokus, Konzentration, mentale Stärke und Klarheit. All das bekommen Menschen in der Zusammenarbeit mit ihm.",
                "Seit mehr als 25 Jahren trainiert, coacht und berät er Spitzensportler und Mannschaften: darunter Handballnationalspieler, Champions-League-Handballer sowie EM- und WM-Teilnehmer aus verschiedenen Sportarten. Er unterstützt Spitzensportler auch nach schweren Verletzungen sowohl emotional, mental als auch körperlich aus der Krise heraus wieder in die volle Leistung zu kommen.",
                "Im Businessleben weist er einen ebenso langen und breiten Erfahrungsschatz auf: Mehr als zwei Jahrzehnte war er im Zürcher Bankwesen in verschiedenen Führungspositionen tätig. Er kennt somit die Herausforderungen, die sowohl Sportler als auch Führungskräfte meistern müssen.",
                "«Häufig weisen die Themen einer Führungsperson Parallelen zu denen von Sportlern auf. Zum Beispiel in puncto Leistungsdruck, Visionen-Umsetzen oder der Forderung nach Höchstleistung. Deshalb unterstütze ich nicht nur Spitzensportler mental, sondern führe auch Menschen im Business zu innerer und mentaler Stärke.»",
                "Von 2021 bis 2024 wurde Nino Paneduro viermal in Folge als «Top 100 Trainer & Coaches in der DACH-Region» in der Rubrik Performance von Seminar.Inside ausgezeichnet. 2025 veröffentlichte er gemeinsam mit Christine Wüest das Buch «Der Handball-Code»."
            ]
        }
    ],
    "certifications": [
        "Dipl. Coach Swiss Coaching Association (SCA)",
        "Dipl. Mentalcoach",
        "Dipl. Mentaltrainer",
        "Dipl. Hypnosetherapeut (NGH National Guild of Hypnotists, Inc. USA, Omni Hypnosis Training Center OHTC)",
        "Dipl. HypnoSport-Experte",
        "Dipl. Aktiv-Wach-Hypnose-Coach",
        "Dipl. Kaufmann KFS",
        "Certificate of Advanced Studies (CAS) in psychologischem und mentalem Training im Sport",
        "Dipl. HypnoPerform-Spezialist",
        "Zertifizierter 9 Levels Trainer",
        "Reiss Motivation Profile (RMP) Master"
    ],
    "pillars": [
        {
            "id": "selbstfuehrung",
            "title": "Innere Stärke entwickeln mit Selbstführung",
            "subtitle": "Erfolgreiche Führung braucht Selbstführung",
            "image": "images/header-selbstfuehrung.jpg",
            "pain_points": [
                "Der Arbeitsalltag ist belastend geworden.",
                "Unser Unternehmen ist im Wandel und ich denke nur ans Business.",
                "Die Ansprüche meiner Mitarbeitenden sind anders geworden.",
                "Wie bekomme ich Arbeit und Familie unter einen Hut?"
            ],
            "summary": "Erfolgreiche Führung basiert in erster Linie auf guter Selbstführung. Wer die Kompetenz hat, sich selbst zu führen, nutzt die verfügbare Zeit besser, priorisiert klarer und beachtet eigene Bedürfnisse. Wir schärfen Ihre Selbstwahrnehmung und richten Ihre Selbstführung neu aus."
        },
        {
            "id": "stressmanagement",
            "title": "Innere Stärke mit dem richtigen Stressmanagement",
            "subtitle": "Balance statt Dauerstress",
            "image": "images/header-stressmanagement.jpg",
            "pain_points": [
                "70-Stunden-Wochen sind keine Ausnahme, die Arbeit stapelt sich.",
                "Auch in der Freizeit wird meist noch gearbeitet statt erholt.",
                "Daueranspannung beeinträchtigt Gesundheit und Entscheidungsqualität.",
                "Das Gefühl, abends nicht mehr herunterfahren zu können."
            ],
            "summary": "Gemeinsam decken wir Ihre Stresstreiber auf und erarbeiten eine Strategie, wie Sie neue Energie gewinnen. Mit Achtsamkeit, Aktiv-Wach-Hypnose, Business-Hypnose und gezielten Entspannungsübungen begegnen Sie dem Dauerstress mit neuer innerer Stärke."
        },
        {
            "id": "selbstwirksamkeit",
            "title": "Innere Stärke durch Selbstwirksamkeit",
            "subtitle": "Selbstwirksamkeit – eine essenzielle Führungskompetenz",
            "image": "images/header-selbstwirksamkeit.jpg",
            "pain_points": [
                "Ich reagiere, aber agiere nicht mehr.",
                "Mir ist die Kontrolle abhandengekommen.",
                "Der Druck von allen Seiten wächst.",
                "Ich fühle mich von den äusseren Umständen getrieben."
            ],
            "summary": "Selbstwirksame Menschen meistern neue Herausforderungen, lösen Aufgaben mit Um- und Weitsicht und bewahren in unklaren Situationen einen kühlen Kopf. In unseren Coachings, Seminaren und Workshops trainieren Sie Ihre Selbstwirksamkeit und nutzen Veränderungen als Chance."
        },
        {
            "id": "zukunftsplanung",
            "title": "Innere Stärke wächst durch Zukunftsgestaltung",
            "subtitle": "Führungskräfte sind Zukunftsgestalter",
            "image": "images/header-zukunftsplanung.jpg",
            "pain_points": [
                "Ich fühle mich fremdgesteuert durch andere und äussere Einflüsse.",
                "Ich stecke im Hamsterrad fest und komme nicht mehr raus.",
                "Die Zukunft ist unsicher und ich weiss nicht, wie ich planen soll.",
                "Meine Ziele rücken immer weiter in die Ferne."
            ],
            "summary": "Veränderungen passieren nicht durch Reden, sondern durch konkrete Handlungen. Wir zeigen Ihnen, wie Sie ausserhalb Ihrer Komfortzone agieren und konkrete Schritte unternehmen, um die Zukunft für sich, Ihr Team und Ihr Unternehmen positiv und souverän zu gestalten."
        }
    ],
    "programs": [
        {
            "title": "1:1 Führungskräfte- & Einzel-Coaching",
            "format": "Individuelles Executive-Sparring im Businesspark Sursee oder Online",
            "methods": ["9 Levels Wertesystem", "Reiss Motivation Profile (RMP)", "Business- & Aktiv-Wach-Hypnose", "Mentale Wettkampf- & Prüfungsstärke"]
        },
        {
            "title": "Team-Workshops & Führungsentwicklung",
            "format": "Massgeschneiderte Halbtages-, Tages- und 2-Tages-Workshops (z. B. TUNE IN & 9 Levels Team-Workshop)",
            "methods": ["Werte-Kompass im Führungsteam", "Praktische Tools für Fokus & Gelassenheit im Daily Business", "Resilienz & Burnout-Prävention"]
        },
        {
            "title": "Impulsreferate, Keynotes & Buch «Der Handball-Code»",
            "format": "Inspirierende Vorträge für Führungstagungen, Kundenanlässe und Verbände",
            "methods": ["Parallelen Spitzensport & Management", "12 echte Geschichten aus Nati & Bundesliga", "Der Kopf entscheidet unter Hochdruck"]
        },
        {
            "title": "MentalFitnessCenter Programme",
            "format": "Kontinuierliches Mental-Training im Alltag",
            "methods": ["Inner Strength Circle (Jahresprogramm)", "45 Minuten über Mittag (Monatlicher Live-Call, letzter Donnerstag 12:30–13:15 Uhr)", "33 Daily Lunch Bites (33 Tage tägliche Impulse)"]
        }
    ],
    "reference_logos": [
        {"name": "Logo Parts GmbH", "file": "images/ref-logoparts.png", "sector": "Markenartikel & Unternehmensberatung"},
        {"name": "Kanton Aargau (AWA & Recht)", "file": "images/ref-kanton-aargau.jpg", "sector": "Öffentliche Verwaltung & Führungsteams"},
        {"name": "Generali Versicherungen", "file": "images/ref-generali.jpg", "sector": "Versicherungswirtschaft & Finanzdienstleistungen"},
        {"name": "Bioanalytica AG", "file": "images/ref-bioanalytica.jpg", "sector": "Medizinische Labordiagnostik & Gesundheitswesen"},
        {"name": "Schweizerischer Turnverband (STV)", "file": "images/ref-stv.jpg", "sector": "Spitzensport & Nationaler Dachverband"},
        {"name": "Soleil-Gesundheitspraxis", "file": "images/ref-soleil.jpg", "sector": "Gesundheit & Therapie"},
        {"name": "Zeitlos Designermode Sursee", "file": "images/ref-zeitlos.jpg", "sector": "Detailhandel & Unternehmertum Sursee"},
        {"name": "Cycling Lounge", "file": "images/ref-cyclinglounge.jpg", "sector": "Radsport, Coaching & Performance"},
        {"name": "MO", "file": "images/ref-mo.jpg", "sector": "KMU & Dienstleistung"}
    ],
    "testimonials": [
        {
            "author": "Jenny Theiler",
            "role": "Inhaberin Logo Parts GmbH",
            "topic": "Prüfungs- & Fokus-Coaching (Christine Wüest)",
            "quote": "Christine Wüest hat mich während der Prüfungsphase für die eidg. Marketingfachfrau sehr unterstützt. Mit ihren wertvollen Tipps und Inputs konnte ich mich optimal auf die Prüfungsphase vorbereiten. Christine vermittelte mir die Stärke und das Selbstvertrauen, so dass ich während den 16.5 Prüfungsstunden den Fokus halten konnte. Für mich war das Coaching ein grosses Puzzleteil zu einem erfolgreichen Resultat. Vielen Dank!"
        },
        {
            "author": "Patrick Binkert",
            "role": "Teamleiter Recht bei Kanton Aargau",
            "topic": "Führungsentwicklung, 9 Levels & Business-Hypnose (Nino Paneduro)",
            "quote": "Ich habe schon viele Führungsentwicklungen gemacht – die Arbeit mit Nino Paneduro überzeugte mich vollends. Das erlernte Wissen der eigenen Werte half mir, meinen eigenen Führungsstil zu erkennen. Als ich mit Nino meine 9 Levels-Auswertung besprach und ich mich in allen Punkten wiedererkannte, waren dies wichtige Erkenntnisse für mich. Klarheit in den Werten, Klarheit in der Weiterentwicklung und Klarheit bei meinen Zielen, das half mir beträchtlich. Im Arbeitsalltag ist man ständig mit Druck konfrontiert. Führung, Projektarbeit, Zeitdruck, Weiterbildung … da sind Lösungen gefragt, die einem effektiv helfen. Nino hat mir angeboten, mit Hypnose zu arbeiten. Ich war sehr kritisch gegenüber dieser Methode, doch wollte ich es erleben. Fast unglaublich, wie schnell sich Körper und Geist durch Hypnose erholen können, wie ich meine Konzentration erhöhen und meinen Führungsalltag effektiver gestalten kann. Ich kann Coaching und Hypnose von Nino Paneduro jedem empfehlen."
        },
        {
            "author": "Urs Keller",
            "role": "Bereichsleiter Amtsstelle Arbeitslosenversicherung, Amt für Wirtschaft und Arbeit (AWA) des Kantons Aargau",
            "topic": "2 Führungs-Workshops mit 9 Levels Wertesystem (Nino Paneduro)",
            "quote": "Mit Nino Paneduro haben wir an zwei Workshops am Thema Führungsentwicklung gearbeitet. Mit dem ganzen Führungsteam haben wir das 9 Levels Wertesystem kennengelernt. Wir haben erfahren, wie eindrücklich und wichtig die Selbsterkenntnisse der Werte im Zusammenhang des eigenen Führungsstils sind. Nino überzeugte mit seiner Fachkompetenz und hat unserem Team viele neue Impulse gegeben. Sie helfen uns, im Daily Business klarer zu agieren. Gerne erinnern wir uns an die lehr- und erkenntnisreichen Workshops im «Herzberg» Uffikon und in Aarau."
        },
        {
            "author": "Manuela Graf",
            "role": "Inhaberin Soleil-Gesundheitspraxis",
            "topic": "TUNE IN Workshop (Christine Wüest & Nino Paneduro)",
            "quote": "Ein herzliches Dankeschön an Christine und Nino für die wertvollen Informationen im TUNE IN Workshop. Die beiden haben zahlreiche, leicht anwendbare Tools aufgezeigt wie Mentale Stärke auf einfache Weise im Alltag gefördert und eingesetzt werden kann. Zudem habe ich wertvolle Tipps erhalten wie ich Alltagsherausforderungen mit mehr Leichtigkeit angehen kann und Ziele nicht nur mental, sondern auch emotional visualisieren kann. In anderen Aufgaben haben die beiden aufgezeigt, wie ich auch in hektischen Zeiten fokussiert und gelassen bleiben kann, mich nicht in Details verzettle, sondern meine Bestleistung abrufen kann."
        },
        {
            "author": "Dario Ferrante",
            "role": "Handball-Torhüter QHL1 & Sportarzt",
            "topic": "Über 10 Jahre Mentalcoaching im Spitzensport & Beruf (Nino Paneduro)",
            "quote": "Seit über 10 Jahren bin ich bei Nino im Mentalcoaching. Ich bin immer wieder erstaunt, wie vielseitige Herausforderungen der Spitzenhandball an einen Athleten stellt. Dass ich dabei Nino an meiner Seite weiss, ist mein grosses Ass im Ärmel. Auch wenn in der Karriereplanung mal etwas nicht wie geplant verläuft, steht mir Nino mit Rat und Tat zur Seite und ich erlebe ein konstantes, persönliches Wachstum dank seinem professionellen Training und Coaching. Auch bei den neuen Herausforderungen des Berufs- und Alltagslebens, welche im Laufe der Handballkarriere immer mehr in den Vordergrund gerückt sind, kann ich mich immer auf Nino verlassen. Nino hilft mir sehr, alles unter einen Hut zu bringen und dabei alle neuen Herausforderungen voller Freude anzugehen."
        },
        {
            "author": "Christoph Anrig",
            "role": "Geschäftsführer BBackSoon, St. Gallen",
            "topic": "Executive Sparring & Werte-Klarheit im Startup-Umfeld (Nino Paneduro)",
            "quote": "Nino versteht es, die eigene Persönlichkeit und den Kopf in Einklang zu bringen. Mit handfesten Methoden und als empathischer Sparring-Partner verhalf er mir zu Klarheit bezüglich meiner Werte und Visionen. Ich konnte meinen Kopf frei kriegen und erlernte mentale Methoden, meiner Persönlichkeit auch in stürmischen Zeiten treu zu bleiben. Gerade als Entrepreneur im Startup-Umfeld eine entscheidende Fähigkeit, stark zu performen."
        },
        {
            "author": "Myriam Petersen",
            "role": "Inhaberin Zeitlos Designermode, Sursee",
            "topic": "Reiss Motivation Profile & Unternehmerinnen-Coaching (Nino Paneduro)",
            "quote": "Danke für das aufschlussreiche Coaching! Durch das Coaching bei Nino konnte ich viele neue Erkenntnisse über mich und meine Lebensmotive gewinnen. Charaktereigenschaften, die mir zwar irgendwie bewusst waren, bekamen plötzlich einen Namen. So sind mir meine starken und schwachen Seiten klarer geworden und ich kann mit ihnen bewusster umgehen. Wiederkehrende Fehler, die ich in der Vergangenheit gemacht habe, sind mir nicht mehr passiert, weil mir bewusst wurde, was abläuft und auf was ich achten muss. Durch das Reiss Motivation Profile kann ich meine Lebensmotive und die der anderen besser verstehen und das hilft mir sehr, mit heiklen Situationen besser umzugehen. Verstanden habe ich aber auch, woher ich meine Kraft beziehe und was ich alles erreicht habe."
        },
        {
            "author": "Maria Katramtzi",
            "role": "Unternehmensberaterin und Marketingstrategin",
            "topic": "Workshops & Mentales Personaltraining (Christine Wüest & Nino Paneduro)",
            "quote": "«Ich schaffe DAS» – Durch meine mentale Stärke habe ich in meinem Leben viele Situationen gemeistert. Als dreifache Mutter, selbstständige Unternehmerin und Ersthelferin ist es wichtig, mental stark zu sein. Mentale Stärke kommt nicht über Nacht – durch tägliches Trainieren setzt sie genau dann ein, wenn man sie braucht. Christine und Nino kann ich als mentale Personaltrainer wärmstens empfehlen. Sie gehen individuell auf dich ein. Die Teilnahme an ihren Workshops ist eine Chance, von dieser langjährigen Expertise zu profitieren. Dankeschön ihr Lieben, dass ihr alle Tipps und Tricks weitergebt."
        },
        {
            "author": "Markus Arnold",
            "role": "ICT Architekt",
            "topic": "9 Levels Wertesystem & Business-Hypnose (Nino Paneduro)",
            "quote": "Eine neue und sehr wertvolle Erfahrung! Meine persönlichen Werte zu kennen und diese als Basis für meine beruflichen und privaten Ziele zu nehmen, sind für meine persönliche Entwicklung sehr hilfreich. Dank der 9-Levels-Methode konnte ich die Unklarheiten, was meinen beruflichen Werdegang betrifft, adressieren und beseitigen. Die offenen Gespräche mit Nino in einer angenehmen Umgebung verhalfen mir zu einer neuen und objektiveren Sichtweise. Die regelmässige Reflexion mit Nino motivierte mich, die besprochenen Punkte umzusetzen. Eine neue und sehr wertvolle Erfahrung war für mich, bestimmte Themen mittels Business-Hypnose anzusehen, umzusetzen und zu verarbeiten. Für mich ist die Zusammenarbeit mit Nino sehr wertvoll und ich empfehle sie gerne weiter."
        },
        {
            "author": "Priska Bürgler",
            "role": "Med. Praxisassistentin",
            "topic": "Stressmanagement-Workshop & Einzel-Training (Nino Paneduro)",
            "quote": "Zum ersten Mal kam ich mit dem Thema Stressmanagement an einem Workshop von Nino in Kontakt. Ich durfte erfahren, wie wichtig mentale Gesundheit für den Alltag ist und wie viele Faktoren meist unbewusst wirken. Nino hat dies klar und effektiv aufgezeigt und ich merkte, dass ich mehr darüber wissen möchte. Aufgrund des Workshops entschied ich mich für ein Coaching und Training bei Nino. Dadurch kann ich nun sehr viel klarer auf meine eigenen Bedürfnisse eingehen und merke einen bewussteren Umgang mit meinen Ressourcen. Nino versteht meine Bedürfnisse und meine Sicht und ich kann Nino Paneduro jedem empfehlen – für mehr Klarheit, Fokus und Energie."
        }
    ]
}

for target_dir in (V1_DIR, V2_DIR):
    (target_dir / "before.json").write_text(
        json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8"
    )

# 2. company.json, config.json, site.json für V1 und V2 schreiben
base_company_data = {
    "slug": "innere-staerke",
    "name": "Wüest + Paneduro",
    "company_name": "Wüest + Paneduro · Innere Stärke entwickeln",
    "legal_name": "Nino Paneduro GmbH",
    "short_name": "Wüest + Paneduro",
    "claim": "Innere Stärke entwickeln",
    "subline": "Mit mehr Resilienz, Fokus und Energie souverän führen",
    "street": "Businesspark Sursee, Allee 1b",
    "zip": "6210",
    "city": "Sursee",
    "canton": "LU",
    "country": "Schweiz",
    "email": "mail@innere-staerke.business",
    "phone": "+41 78 606 20 56",
    "phone_secondary": "+41 79 468 21 46",
    "phone_clean": "+41786062056",
    "website": "https://www.innere-staerke.business",
    "industry": "Executive Coaching, Führungsentwicklung & Mentaltraining",
    "industry_id": "b2b_fuehrung_beratung",
    "industry_label": "Mentoren, Coaches & Ratgeber für Führungskräfte und Unternehmen",
    "work_category_label": "Coaching, Workshops & Referenzen",
    "studio_title": "WEBPILOT STUDIO",
    "is_website_studio": True,
    "host_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/cockpit?token=innerestaerke2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/",
    "copyright": "© 2026 Nino Paneduro GmbH (Wüest + Paneduro · Businesspark Sursee). Alle Rechte vorbehalten.",
    "hosting_status": "Live-Betrieb & Hosting: Schweizer Edge · WebPilot Studio v4.0",
    "linkedin_profile": "https://www.linkedin.com/company/mentalfitnesscenter/",
    "facebook_profile": "https://www.facebook.com/groups/mentalfitnesscenter/"
}

(V1_DIR / "company.json").write_text(json.dumps(base_company_data, indent=2, ensure_ascii=False), encoding="utf-8")
v1_config = dict(base_company_data)
v1_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/",
    "cockpit_token": "innerestaerke2026",
    "template": "executive-coaching-flagship-v1",
    "pages": ["index.html", "angebot.html", "ueber-uns.html", "referenzen.html", "kontakt.html"]
})
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-innere-staerke",
    "public_slug": "innere-staerke",
    "token": "innerestaerke2026",
    "name": "Wüest + Paneduro · Innere Stärke entwickeln",
    "Updated": "2026-11-03",
    "PagesCount": 5,
    "ReferencesCount": 9,
    "TestimonialsCount": 10
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_company = dict(base_company_data)
v2_company.update({
    "slug": "innere-staerke-v2",
    "name": "Wüest + Paneduro (Zeigeversion)",
    "host_url": "https://vorschau.magnet-xs.ch/innere-staerke-v2/cockpit?token=innerestaerke2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/innere-staerke-v2/"
})
(V2_DIR / "company.json").write_text(json.dumps(v2_company, indent=2, ensure_ascii=False), encoding="utf-8")
v2_config = dict(v2_company)
v2_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/innere-staerke-v2/",
    "cockpit_token": "innerestaerke2026",
    "template": "executive-coaching-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-innere-staerke-v2",
    "public_slug": "innere-staerke-v2",
    "token": "innerestaerke2026",
    "name": "Wüest + Paneduro (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-03",
    "PagesCount": 2,
    "ReferencesCount": 9,
    "TestimonialsCount": 10
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      --charcoal: #222221;
      --charcoal-deep: #161615;
      --charcoal-mid: #3A3A39;
      --gold: #F9B231;
      --gold-hover: #FBBF24;
      --gold-dark: #9A5800;
      --gold-soft: #FEF7E6;
      --gold-border: #F5C451;
      --crimson: #AE031D;
      --crimson-soft: #FDF2F4;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #F9FAFB;
      --bg-card: #FFFFFF;
      --bg-Warm: #F4F3EF;
      --text-main: #181817;
      --text-body: #374151;
      --text-muted: #4B5563;
      --border-light: #E5E7EB;
      --border-strong: #D1D5DB;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(24, 24, 23, 0.05);
      --shadow-md: 0 12px 30px rgba(24, 24, 23, 0.09);
      --shadow-lg: 0 20px 44px rgba(24, 24, 23, 0.16);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(249, 178, 49, 0.28);
      color: #181817;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      overflow-x: hidden;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.62;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      font-variant-numeric: tabular-nums;
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.18s ease, background-color 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
    }

    ul {
      list-style: none;
    }

    .container {
      width: 100%;
      max-width: var(--container);
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Freistehende Marken-Kicker (#UI-01: Barlow Bold, 0 JetBrains Mono, 0 //) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--gold-dark);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      margin-bottom: 12px;
    }
    .section-kicker.kicker-light {
      color: var(--gold);
    }

    h1, h2, h3, h4 {
      font-family: 'Barlow', sans-serif;
      color: var(--text-main);
      line-height: 1.18;
      letter-spacing: -0.015em;
    }

    .section-head {
      max-width: 780px;
      margin-bottom: 44px;
    }
    .section-title {
      font-size: clamp(1.85rem, 3.1vw, 2.55rem);
      font-weight: 800;
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.03rem;
      color: var(--text-body);
      line-height: 1.65;
    }

    section {
      padding: 80px 0;
      position: relative;
    }

    /* 1-Klick-Versions-Umschalter oben (V1 <-> V2) */
    .wp-version-bar {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border-bottom: 2px solid var(--gold);
      font-size: 0.8rem;
      position: relative;
      z-index: 1003;
      padding: 9px 0;
    }
    .wp-version-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }
    .wp-version-info {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      font-size: 0.8rem;
      font-weight: 600;
      color: #E5E7EB;
    }
    .wp-version-pill-group {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .wp-ver-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 6px 12px;
      min-height: 34px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.22);
      background-color: rgba(255, 255, 255, 0.07);
      color: #F3F4F6;
      line-height: 1.25;
    }
    .wp-ver-btn.is-active {
      background-color: var(--gold);
      color: #161615;
      border-color: var(--gold);
      font-weight: 800;
    }
    .wp-ver-btn.is-switch {
      border-color: var(--gold);
      color: var(--gold);
      background-color: rgba(249, 178, 49, 0.12);
    }
    .wp-ver-btn.is-switch:hover {
      background-color: var(--gold);
      color: #161615;
    }

    /* Sub-Topbar (Standort Sursee & Direktkontakt) */
    .top-bar {
      background-color: var(--charcoal);
      color: #E5E7EB;
      font-size: 0.78rem;
      padding: 8px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .top-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .top-bar-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background-color: rgba(249, 178, 49, 0.18);
      color: var(--gold);
      border: 1px solid rgba(249, 178, 49, 0.45);
      font-family: 'Barlow', sans-serif;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }
    .top-bar-links {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .top-bar-links a {
      color: #E5E7EB;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: var(--gold);
    }

    /* Sticky Main Header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(24, 24, 23, 0.04);
    }
    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      min-height: 76px;
      padding: 8px 0;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }
    .brand-logo {
      width: 52px;
      height: 52px;
      object-fit: contain;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Barlow', sans-serif;
      font-size: 1.12rem;
      font-weight: 800;
      color: var(--charcoal);
      letter-spacing: -0.01em;
      line-height: 1.15;
    }
    .brand-sub {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--gold-dark);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-top: 2px;
    }

    .main-nav {
      display: flex;
      align-items: center;
      gap: 22px;
      flex-wrap: nowrap;
      white-space: nowrap;
    }
    .nav-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text-body);
      padding: 6px 2px;
      min-height: 36px;
      border-radius: 0;
      border: none;
      border-bottom: 2px solid transparent;
      background: transparent;
      white-space: nowrap;
      cursor: pointer;
    }
    .nav-link:hover,
    .nav-link.active {
      color: var(--charcoal-deep);
      background: transparent;
      border-bottom-color: var(--gold-dark);
    }
    .nav-link-preview {
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 2px dashed #9CA3AF;
      font-size: 0.88rem;
    }
    .nav-link-preview:hover {
      color: var(--charcoal-deep);
      background-color: var(--gold-soft);
      border-color: var(--gold-dark);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Buttons (#UI-01: 8px radius, high contrast) */
    .btn-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      padding: 12px 20px;
      min-height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid transparent;
      cursor: pointer;
      text-align: center;
      line-height: 1.25;
      transition: all 0.18s ease;
    }
    .btn-cta svg {
      flex-shrink: 0;
    }
    .btn-cta-gold {
      background-color: var(--gold);
      color: #161615;
      border-color: var(--gold);
      font-weight: 800;
    }
    .btn-cta-gold:hover {
      background-color: var(--gold-hover);
      color: #161615;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: var(--charcoal);
      color: #FFFFFF;
      border-color: var(--charcoal);
    }
    .btn-cta-primary:hover {
      background-color: var(--charcoal-deep);
      color: var(--gold);
      border-color: var(--charcoal-deep);
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--charcoal);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--charcoal);
      background-color: var(--bg-Warm);
    }
    .btn-cta-outline-light {
      background-color: rgba(255, 255, 255, 0.08);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.28);
    }
    .btn-cta-outline-light:hover {
      background-color: rgba(255, 255, 255, 0.16);
      border-color: var(--gold);
    }
    .btn-sm {
      font-size: 0.84rem;
      padding: 9px 15px;
      min-height: 40px;
    }

    /* Mobile Burger & Drawer */
    .mobile-toggle {
      display: none;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      color: var(--charcoal);
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: var(--charcoal-deep);
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Barlow', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #F9FAFB;
      padding: 12px 14px;
      min-height: 44px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      text-align: left;
      width: 100%;
      cursor: pointer;
    }
    .mobile-drawer button.mobile-nav-btn {
      color: var(--gold);
      border-style: dashed;
      border-color: rgba(249, 178, 49, 0.55);
    }

    /* Hero Section – Hell, klar & freundlich wie innere-staerke.business */
    .hero-section {
      background: linear-gradient(135deg, #ffffff 0%, #f8f6f2 55%, #f1ede6 100%);
      background-color: #f8f6f2;
      color: #181817;
      padding: 72px 0 84px;
      border-bottom: 3px solid var(--gold);
      overflow: hidden;
    }
    .hero-section .section-kicker.kicker-light {
      color: var(--crimson);
    }
    .hero-section .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: #181817;
      border-color: #CBD5E1;
    }
    .hero-section .btn-cta-outline-light:hover {
      background-color: var(--gold-soft);
      color: #181817;
      border-color: var(--gold-dark);
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 44px;
      align-items: stretch;
    }
    .hero-grid > div:first-child {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-title {
      font-size: clamp(2.15rem, 3.8vw, 3.25rem);
      font-weight: 800;
      color: #181817;
      line-height: 1.12;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: var(--crimson);
    }
    .hero-lead {
      font-size: 1.06rem;
      color: #374151;
      line-height: 1.68;
      margin-bottom: 26px;
    }
    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 28px;
    }
    .hero-actions:last-child,
    .hero-badges:last-child {
      margin-top: auto;
      margin-bottom: 0;
    }
    .hero-actions .btn-cta {
      padding: 11px 16px;
      font-size: 0.86rem;
      white-space: nowrap;
    }
    .hero-badges {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }
    .hero-badge-card {
      background-color: #FFFFFF;
      border: 1px solid #E5E7EB;
      border-left: 3px solid var(--crimson);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2px;
      box-shadow: var(--shadow-sm);
    }
    .hero-badge-val {
      font-family: 'Barlow', sans-serif;
      font-size: 0.92rem;
      font-weight: 800;
      color: #181817;
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #4B5563;
      line-height: 1.35;
    }

    .hero-media-card {
      background-color: #FFFFFF;
      border: 1px solid #E5E7EB;
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .hero-media-card img {
      width: 100%;
      height: 260px;
      min-height: 260px;
      flex: 1 1 auto;
      object-fit: cover;
      object-position: center top;
    }
    .hero-media-caption {
      padding: 16px 20px;
      background-color: #F8F6F2;
      border-top: 1px solid #E5E7EB;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .hero-media-caption .top-bar-badge {
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border-color: var(--gold-border);
    }

    /* Universal Symmetric Grids (#UI-14: Zero Ragged Edges & Equal Height) */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
      align-items: stretch;
    }
    .grid-2 > :last-child:nth-child(odd) {
      grid-column: 1 / -1;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      align-items: stretch;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      align-items: stretch;
    }

    /* Cards */
    .content-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .content-card.card-accent-top {
      border-top: 4px solid var(--gold);
    }
    .content-card.card-dark {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border-color: rgba(255, 255, 255, 0.14);
    }
    .content-card.card-dark h3 {
      color: #FFFFFF;
    }

    .card-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }
    .meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
    }
    .icon-box {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .check-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 8px;
    }
    .check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.92rem;
      color: var(--text-body);
      line-height: 1.5;
    }
    .check-item svg {
      color: var(--gold-dark);
      flex-shrink: 0;
      margin-top: 3px;
    }
    .card-dark .check-item {
      color: #E5E7EB;
    }
    .card-dark .check-item svg {
      color: var(--gold);
    }

    /* Pillar Media Cards */
    .pillar-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .pillar-img-wrap {
      width: 100%;
      height: 210px;
      overflow: hidden;
      background-color: var(--charcoal);
      position: relative;
    }
    .pillar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }
    .pillar-body {
      padding: 24px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Founder Cards */
    .founder-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .founder-top {
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: 22px;
      padding: 26px 26px 0;
      align-items: start;
    }
    .founder-portrait {
      width: 100%;
      height: 230px;
      object-fit: cover;
      object-position: center top;
      border-radius: var(--radius-md);
      border: 2px solid var(--gold);
    }
    .founder-body {
      padding: 20px 26px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Reference Logos Grid (9 Logos -> 3x3 on Desktop & Laptop, 1 col on Mobile) */
    .ref-logos-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      align-items: stretch;
    }
    .ref-logo-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      gap: 12px;
      box-shadow: var(--shadow-sm);
      height: 100%;
    }
    .ref-logo-stage {
      width: 100%;
      height: 84px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      background-color: #FFFFFF;
    }
    .ref-logo-stage img {
      max-height: 72px;
      max-width: 180px;
      width: auto;
      height: auto;
      object-fit: contain;
    }
    .ref-logo-name {
      font-family: 'Barlow', sans-serif;
      font-size: 0.94rem;
      font-weight: 800;
      color: var(--charcoal);
    }
    .ref-logo-sector {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    /* Testimonial Cards */
    .testimonial-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-top: 3px solid var(--gold);
      border-radius: var(--radius-md);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .testimonial-quote {
      font-size: 0.93rem;
      color: var(--text-body);
      line-height: 1.65;
      font-style: italic;
    }
    .testimonial-author-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-top: 14px;
      border-top: 1px solid var(--border-light);
    }
    .testimonial-author {
      font-family: 'Barlow', sans-serif;
      font-size: 0.98rem;
      font-weight: 800;
      color: var(--charcoal);
    }
    .testimonial-role {
      font-size: 0.8rem;
      color: var(--gold-dark);
      font-weight: 600;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) Spezifische Styles (#UI-03 Kunden-Sprache) */
    .preview-scope-section {
      background-color: #EFECE6;
      border-top: 2px dashed var(--charcoal-mid);
      border-bottom: 2px dashed var(--charcoal-mid);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border: 2px dashed var(--gold);
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #6B7280;
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      box-shadow: var(--shadow-sm);
      height: 100%;
    }
    .preview-status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--gold-soft);
      border: 1px solid var(--gold-border);
      color: var(--gold-dark);
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }

    /* Footer */
    .site-footer {
      background-color: var(--charcoal-deep);
      color: #E5E7EB;
      padding: 68px 0 36px;
      border-top: 4px solid var(--gold);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 36px;
      padding-bottom: 42px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }
    .footer-title {
      font-family: 'Barlow', sans-serif;
      font-size: 0.94rem;
      font-weight: 800;
      color: #FFFFFF;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 16px;
    }
    .footer-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .footer-list a,
    .footer-list button {
      color: #D1D5DB;
      font-size: 0.88rem;
      background: none;
      border: none;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
      padding: 5px 0;
      min-height: 34px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .footer-list a:hover,
    .footer-list button:hover {
      color: var(--gold);
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #9CA3AF;
    }
    .footer-bottom a {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 4px 0;
    }

    /* Modals (#wpBlueprintModal & #wpImpressumModal) */
    .wp-modal-backdrop {
      position: fixed;
      inset: 0;
      background-color: rgba(15, 15, 14, 0.76);
      backdrop-filter: blur(4px);
      z-index: 9998;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      overflow-y: auto;
    }
    .wp-modal-backdrop.open {
      display: flex;
    }
    .wp-modal-dialog {
      background-color: #FFFFFF;
      color: var(--text-main);
      border: 2px solid var(--gold);
      border-radius: var(--radius-md);
      max-width: 650px;
      width: 100%;
      padding: 28px;
      position: relative;
      box-shadow: var(--shadow-lg);
      max-height: 90vh;
      overflow-y: auto;
    }
    .wp-modal-close {
      position: absolute;
      top: 16px;
      right: 16px;
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: var(--bg-page);
      color: var(--charcoal);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .wp-modal-checklist {
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .wp-modal-check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.86rem;
      color: var(--text-body);
    }
    .wp-modal-check-item svg {
      color: var(--gold-dark);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* 3-Schritte Smart-Anfrage Assistent (kontakt.html) */
    .contact-layout {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 38px;
      align-items: start;
    }
    .contact-info-panel {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
      box-shadow: var(--shadow-sm);
    }
    .contact-direct-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 20px;
    }
    .contact-direct-item {
      padding: 12px 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--gold);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Barlow', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--gold-dark);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--charcoal);
      margin-top: 2px;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.82rem;
      margin-top: 2px;
    }

    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--charcoal);
      border-radius: var(--radius-md);
      padding: 30px;
      box-shadow: var(--shadow-md);
    }
    .wp-stepper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 22px;
      padding: 6px;
      background-color: var(--bg-Warm);
      border-radius: var(--radius-md);
    }
    .wp-step-pill {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 8px;
      border-radius: var(--radius-sm);
      font-family: 'Barlow', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: var(--charcoal);
      color: var(--gold);
    }
    .wp-step-pill.done {
      background-color: var(--green-soft);
      color: #166534;
    }
    .wp-step-num {
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.16);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.74rem;
      font-weight: 800;
      flex-shrink: 0;
    }

    .wp-step-pane {
      display: none;
    }
    .wp-step-pane.active {
      display: block;
    }

    .wp-role-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 20px;
      align-items: stretch;
    }
    .wp-role-tile {
      background-color: var(--bg-page);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 14px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      transition: all 0.18s ease;
      font-family: inherit;
      min-height: 92px;
    }
    .wp-role-tile:hover {
      border-color: var(--charcoal);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--charcoal);
      background-color: var(--gold-soft);
    }
    .wp-role-head {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .wp-role-icon {
      width: 28px;
      height: 28px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: 'Barlow', sans-serif;
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
    }
    .wp-role-desc {
      font-size: 0.77rem;
      color: var(--text-body);
      line-height: 1.42;
    }

    .form-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      align-items: stretch;
    }
    .form-field {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 6px;
    }
    .form-label {
      font-family: 'Barlow', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--charcoal);
      line-height: 1.3;
    }
    .form-input,
    .form-textarea {
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.9rem;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      min-height: 44px;
    }
    .form-input:focus,
    .form-textarea:focus {
      outline: none;
      border-color: var(--charcoal);
      box-shadow: 0 0 0 3px rgba(249, 178, 49, 0.25);
    }
    .form-textarea {
      min-height: 100px;
      resize: vertical;
    }

    .wp-upload-zone {
      border: 1px dashed var(--border-strong);
      background-color: var(--bg-page);
      border-radius: var(--radius-md);
      padding: 14px;
    }
    .wp-upload-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 14px;
      min-height: 42px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      font-family: 'Barlow', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--charcoal);
      cursor: pointer;
    }
    .wp-photo-thumbs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
    }
    .wp-thumb-item {
      position: relative;
      width: 72px;
      height: 72px;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 1px solid var(--border-strong);
    }
    .wp-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .wp-thumb-remove {
      position: absolute;
      top: 2px;
      right: 2px;
      width: 22px;
      height: 22px;
      background-color: var(--charcoal);
      color: #FFFFFF;
      border: none;
      border-radius: var(--radius-sm);
      font-size: 0.72rem;
      cursor: pointer;
    }

    .wp-plz-badge {
      display: none;
      align-items: center;
      gap: 8px;
      margin-top: 6px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
    }
    .wp-plz-badge.in-area {
      display: flex;
      background-color: var(--green-soft);
      color: #166534;
      border: 1px solid #86EFAC;
    }

    .wp-selftest-banner {
      background-color: var(--gold-soft);
      border: 1px solid var(--gold-border);
      border-left: 4px solid var(--gold-dark);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 0.8rem;
      color: #78350F;
      margin-bottom: 16px;
    }

    .wp-success-box {
      display: none;
      flex-direction: column;
      gap: 16px;
      padding: 24px;
      background-color: var(--bg-page);
      border: 2px solid var(--green);
      border-radius: var(--radius-md);
    }
    .wp-success-box.visible {
      display: flex;
    }
    .wp-wa-preview {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.82rem;
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 4px solid var(--green);
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      white-space: pre-wrap;
      color: var(--text-main);
    }

    @media (max-width: 1080px) {
      .hero-grid,
      .contact-layout,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .grid-4 {
        grid-template-columns: repeat(2, 1fr);
      }
      .main-nav {
        display: none;
      }
      .mobile-toggle {
        display: inline-flex;
      }
    }

    @media (max-width: 768px) {
      section {
        padding: 56px 0;
      }
      .grid-2,
      .grid-3,
      .grid-4,
      .ref-logos-grid,
      .hero-badges,
      .wp-role-grid,
      .form-grid-2,
      .wp-stepper,
      .founder-top {
        grid-template-columns: 1fr;
      }
      .header-actions .btn-cta {
        display: none;
      }
      .hero-actions .btn-cta {
        white-space: normal;
        width: 100%;
      }
      .hero-media-card img {
        height: 270px;
      }
      .founder-portrait {
        height: 250px;
      }
      .wizard-card,
      .content-card {
        padding: 20px;
      }
      .wp-version-inner {
        flex-direction: column;
        align-items: stretch;
      }
      .wp-version-pill-group {
        width: 100%;
      }
      .wp-ver-btn {
        flex: 1 1 auto;
      }
    }
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_COMPASS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_ZAP = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_SPARKLES = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>'
SVG_MAP_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'


def render_reference_logos_grid() -> str:
    cards = []
    for ref in BEFORE_INVENTORY["reference_logos"]:
        cards.append(f"""
        <div class="ref-logo-card">
          <div class="ref-logo-stage">
            <img src="{ref['file']}" alt="{ref['name']}" loading="lazy" decoding="async">
          </div>
          <div>
            <div class="ref-logo-name">{ref['name']}</div>
            <div class="ref-logo-sector">{ref['sector']}</div>
          </div>
        </div>""")
    return '<div class="ref-logos-grid">\n' + "\n".join(cards) + "\n      </div>"


def render_testimonials_grid(limit: int = 10) -> str:
    cards = []
    for idx, t in enumerate(BEFORE_INVENTORY["testimonials"][:limit]):
        cards.append(f"""
        <div class="testimonial-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">{t['topic']}</span>
              <span style="color:var(--gold-dark);font-family:'Barlow',sans-serif;font-size:0.78rem;font-weight:800;">Verifizierte Stimme #{idx+1}</span>
            </div>
            <p class="testimonial-quote">«{t['quote']}»</p>
          </div>
          <div class="testimonial-author-row">
            <div>
              <div class="testimonial-author">{t['author']}</div>
              <div class="testimonial-role">{t['role']}</div>
            </div>
            <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-outline btn-sm">
              <span>Dialog starten</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM & DATENSCHUTZ MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · NINO PANEDURO GMBH</div>
      <h3 id="wpImpTitle" style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz (Wüest + Paneduro)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Nino Paneduro GmbH (Wüest + Paneduro · Innere Stärke entwickeln)</strong><br>
          Businesspark Sursee · Allee 1b · CH-6210 Sursee<br>
          Telefon: +41 78 606 20 56 / +41 79 468 21 46 · E-Mail: mail@innere-staerke.business
        </div>
        <p>
          <strong>Handelsregister &amp; Vertretung:</strong><br>
          Eingetragen im Handelsregister des Kantons Luzern (Unternehmensidentifikationsnummer: <strong>CHE-279.321.936</strong>). Vertreten durch <strong>Antonino Paneduro</strong>, Vorsitzender der Geschäftsführung, und <strong>Christine Wüest Paneduro</strong>, Geschäftsführerin.<br>
          Schweizerische Mehrwertsteuernummer: <strong>CHE-279.321.936 MWST</strong>.
        </p>
        <p>
          <strong>Urheberrecht &amp; Bildnachweise:</strong><br>
          Alle auf dieser Website abgebildeten Inhalte (Texte, Konzepte, Porträtfotos von Uwe Klössing und Grafiken) stehen im Eigentum der Nino Paneduro GmbH respektive der jeweiligen Rechteinhaber.
        </p>
        <p>
          <strong>Datenschutz (CH-DSG / DSGVO):</strong><br>
          Personenbezogene Angaben aus dem 3-Schritte Smart-Anfrage-Assistenten werden ausschliesslich zur Beantwortung Ihrer Anfrage und zur Erstellung Ihres persönlichen 1-Seiten-Anfrage-Dossiers verwendet und niemals an unbefugte Dritte weitergegeben.
        </p>
      </div>
      <div style="margin-top:18px;display:flex;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseImpressumModal()">
          <span>Schliessen</span>
        </button>
      </div>
    </div>
  </div>"""


COMMON_UI_JS = """
  <script>
    function wpToggleMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.toggle('open');
    }
    function wpCloseMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.remove('open');
    }
    function wpOpenImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.add('open');
    }
    function wpCloseImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.remove('open');
    }
    function wpOpenBlueprintModal(title, category, focus) {
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var tEl = document.getElementById('wpBpTitle');
      var cEl = document.getElementById('wpBpCategory');
      var fEl = document.getElementById('wpBpContact');
      if (tEl && title) tEl.textContent = title;
      if (cEl && category) cEl.textContent = 'Themenbereich: ' + category;
      if (fEl && focus) fEl.textContent = 'Begleitung & Umsetzung: ' + focus;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        wpCloseImpressumModal();
        wpCloseBlueprintModal();
        wpCloseMobileMenu();
      }
    });
  </script>
"""


def render_v1_shell(filename: str, page_title: str, active_nav: str, body_html: str) -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_angebot = "active" if active_nav == "angebot" else ""
    nav_ueber = "active" if active_nav == "ueber-uns" else ""
    nav_ref = "active" if active_nav == "referenzen" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v2_href = "/innere-staerke-v2/kontakt.html" if filename == "kontakt.html" else "/innere-staerke-v2/"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Wüest + Paneduro · Innere Stärke entwickeln. Mentoren, Coaches &amp; Ratgeber für Führungskräfte, Teams und Unternehmen im Businesspark Sursee &amp; schweizweit.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">BUSINESSPARK SURSEE · ALLEE 1B · CH-6210 SURSEE</span>
        <span data-slot="topbar_sub">Mentoren, Coaches &amp; Ratgeber für Führungskräfte, Unternehmen &amp; Spitzensport</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41786062056">{SVG_PHONE} <span>+41 78 606 20 56</span></a>
        <a href="mailto:mail@innere-staerke.business">{SVG_MAIL} <span>mail@innere-staerke.business</span></a>
        <a href="https://www.linkedin.com/company/mentalfitnesscenter/" target="_blank" rel="noopener noreferrer">LinkedIn MentalFitnessCenter</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Wüest + Paneduro Startseite">
        <img src="images/logo.svg" alt="Wüest + Paneduro · Innere Stärke entwickeln" class="brand-logo" width="52" height="52" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">WÜEST + PANEDURO</span>
          <span class="brand-sub" data-slot="brand_sub">INNERE STÄRKE ENTWICKELN</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="angebot.html" class="nav-link {nav_angebot}" data-nav-href="angebot.html">Angebot</a>
        <a href="ueber-uns.html" class="nav-link {nav_ueber}" data-nav-href="ueber-uns.html">Über uns</a>
        <a href="referenzen.html" class="nav-link {nav_ref}" data-nav-href="referenzen.html">Referenzen</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" data-slot="header_cta">
          <span>Kennenlerntermin vereinbaren</span>
          {SVG_ARROW}
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

  </header>
  <div class="mobile-drawer" id="mobileDrawer">
    <a href="index.html" onclick="wpCloseMobileMenu()">Startseite</a>
    <a href="angebot.html" onclick="wpCloseMobileMenu()">Angebot, Programme &amp; 4 Säulen</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über uns: Christine Wüest &amp; Nino Paneduro</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Referenzen &amp; Alle 10 Kundenstimmen</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage &amp; Kontakt</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo.svg" alt="Wüest + Paneduro Logo" width="48" height="48" loading="lazy" decoding="async" style="border-radius:4px;">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.1rem;color:#FFFFFF;">WÜEST + PANEDURO</div>
              <div style="font-size:0.76rem;color:var(--gold);font-weight:700;">INNERE STÄRKE ENTWICKELN · SURSEE</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#D1D5DB;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Als Mentoren, Coaches und Ratgeber begleiten Christine Wüest und Nino Paneduro Führungskräfte, Teams und Unternehmen auf dem Weg zu innerer Stärke, Resilienz und nachhaltiger Wirksamkeit.
          </p>
          <div style="font-size:0.84rem;color:#F3F4F6;font-weight:600;">
            Nino Paneduro GmbH · Businesspark Sursee · Allee 1b · CH-6210 Sursee
          </div>
        </div>

        <div>
          <div class="footer-title">4 Säulen der Methode</div>
          <ul class="footer-list">
            <li><a href="angebot.html#selbstfuehrung">1. Selbstführung im Wandel</a></li>
            <li><a href="angebot.html#stressmanagement">2. Gesundes Stressmanagement</a></li>
            <li><a href="angebot.html#selbstwirksamkeit">3. Souveräne Selbstwirksamkeit</a></li>
            <li><a href="angebot.html#zukunftsplanung">4. Aktive Zukunftsgestaltung</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Angebot &amp; Programme</div>
          <ul class="footer-list">
            <li><a href="angebot.html#programme">1:1 Führungskräfte-Coaching</a></li>
            <li><a href="angebot.html#programme">Unternehmens-Workshops &amp; 9 Levels</a></li>
            <li><a href="angebot.html#handball-code">Keynotes &amp; Buch «Der Handball-Code»</a></li>
            <li><a href="angebot.html#mentalfitnesscenter">MentalFitnessCenter &amp; Lunch Bites</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41786062056">+41 78 606 20 56 (Direktwahl)</a></li>
            <li><a href="mailto:mail@innere-staerke.business">mail@innere-staerke.business</a></li>
            <li><a href="kontakt.html" style="color:var(--gold);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz (CHE-279.321.936)</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Nino Paneduro GmbH (Wüest + Paneduro · Businesspark Sursee, Allee 1b, CH-6210 Sursee).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold);font-weight:700;">Kennenlerntermin &amp; Smart-Anfrage</a>
          <a href="referenzen.html" style="color:#E5E7EB;">Alle 10 Kundenstimmen</a>
        </div>
      </div>
    </div>
  </footer>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""


def render_v2_shell(filename: str, page_title: str, active_nav: str, body_html: str) -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v1_href = "/innere-staerke/kontakt.html" if filename == "kontakt.html" else "/innere-staerke/"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Unverbindlicher Vorschau-Entwurf (Zeigeversion) für Wüest + Paneduro: 2 Beispiel-Seiten sind bereits ausgearbeitet – 3 weitere Themenbereiche folgen beim Ausbau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">BUSINESSPARK SURSEE · ALLEE 1B · CH-6210 SURSEE</span>
        <span data-slot="topbar_sub">Mentoren, Coaches &amp; Ratgeber für Führungskräfte, Unternehmen &amp; Spitzensport</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41786062056">{SVG_PHONE} <span>+41 78 606 20 56</span></a>
        <a href="mailto:mail@innere-staerke.business">{SVG_MAIL} <span>mail@innere-staerke.business</span></a>
        <a href="https://www.linkedin.com/company/mentalfitnesscenter/" target="_blank" rel="noopener noreferrer">LinkedIn MentalFitnessCenter</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (ZEIGEVERSION MIT KUNDENFREUNDLICHEN VORSCHAU-HINWEISEN) -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Wüest + Paneduro Startseite">
        <img src="images/logo.svg" alt="Wüest + Paneduro · Innere Stärke entwickeln" class="brand-logo" width="52" height="52" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">WÜEST + PANEDURO</span>
          <span class="brand-sub" data-slot="brand_sub">INNERE STÄRKE ENTWICKELN</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Angebots-Vertiefung &amp; Seminar-Programme', '1:1 Executive-Coaching, 9 Levels Workshops, Hypnose &amp; MentalFitnessCenter', 'Christine Wüest &amp; Nino Paneduro')">
          <span>Angebot</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Über uns, Werdegang &amp; 11 Zertifizierungen', 'Ausführliche Porträts von Christine Wüest &amp; Nino Paneduro sowie Businesspark Sursee', 'Christine Wüest &amp; Nino Paneduro')">
          <span>Über uns</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Detaillierte Fallstudien &amp; Alle 10 Teilnehmerstimmen', 'Referenz-Berichte aus Verwaltung, Wirtschaft &amp; Spitzensport', 'Christine Wüest &amp; Nino Paneduro')">
          <span>Referenzen</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Kontakt</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" data-slot="header_cta">
          <span>Smart-Anfrage testen</span>
          {SVG_ARROW}
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

  </header>
  <div class="mobile-drawer" id="mobileDrawer">
    <a href="index.html" onclick="wpCloseMobileMenu()">Startseite (Beispiel-Seite ausgearbeitet)</a>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Angebots-Vertiefung &amp; Seminar-Programme', '1:1 Executive-Coaching, 9 Levels Workshops &amp; MentalFitnessCenter', 'Christine Wüest &amp; Nino Paneduro')">
      <span>Angebot</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Über uns, Werdegang &amp; 11 Zertifizierungen', 'Ausführliche Porträts von Christine Wüest &amp; Nino Paneduro', 'Christine Wüest &amp; Nino Paneduro')">
      <span>Über uns &amp; Werdegang (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Detaillierte Fallstudien &amp; Alle 10 Teilnehmerstimmen', 'Referenz-Berichte aus Verwaltung, Wirtschaft &amp; Spitzensport', 'Christine Wüest &amp; Nino Paneduro')">
      <span>Referenzen &amp; Kundenstimmen (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage (Live-Demo)</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER (ZEIGEVERSION) -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo.svg" alt="Wüest + Paneduro Logo" width="48" height="48" loading="lazy" decoding="async" style="border-radius:4px;">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.1rem;color:#FFFFFF;">WÜEST + PANEDURO</div>
              <div style="font-size:0.76rem;color:var(--gold);font-weight:700;">VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#D1D5DB;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Unverbindlicher Vorschau-Entwurf für Wüest + Paneduro: 2 Beispiel-Seiten (Startseite &amp; 3-Schritte Smart-Anfrage) sind bereits ausgearbeitet – 3 weitere Themenbereiche folgen beim gemeinsamen Ausbau.
          </p>
          <div style="font-size:0.84rem;color:#F3F4F6;font-weight:600;">
            Businesspark Sursee · Allee 1b · CH-6210 Sursee · +41 78 606 20 56
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits ausgearbeitet (Live)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Hero &amp; 4 Methoden-Säulen</a></li>
            <li><a href="index.html#gruender">Gründer-Vorstellung: Wüest + Paneduro</a></li>
            <li><a href="index.html#referenzlogos">Alle 9 Original-Referenzlogos</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (Live-Demo)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Folgen beim gemeinsamen Ausbau</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Angebots-Vertiefung &amp; Seminar-Programme', '1:1 Executive-Coaching, 9 Levels Workshops &amp; Business-Hypnose', 'Christine Wüest &amp; Nino Paneduro')">Angebots-Vertiefung &amp; Programme</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Detaillierte Fallstudien &amp; Teilnehmerstimmen', 'Alle 10 Kundenstimmen &amp; Praxis-Berichte im Detail', 'Christine Wüest &amp; Nino Paneduro')">Fallstudien &amp; 10 Teilnehmerstimmen</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('MentalFitnessCenter &amp; Impulse', 'Inner Strength Circle, 45 Minuten über Mittag, 33 Daily Lunch Bites &amp; Buch «Der Handball-Code»', 'Christine Wüest &amp; Nino Paneduro')">MentalFitnessCenter &amp; Impulse</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41786062056">+41 78 606 20 56 (Direktwahl)</a></li>
            <li><a href="mailto:mail@innere-staerke.business">mail@innere-staerke.business</a></li>
            <li><a href="kontakt.html" style="color:var(--gold);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Nino Paneduro GmbH (Wüest + Paneduro · Sursee) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold);font-weight:700;">Smart-Anfrage testen</a>
          <a href="index.html#weitere-themenbereiche" style="color:#E5E7EB;">Weitere Themenbereiche</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- KUNDENFREUNDLICHES VORSCHAU-MODAL (#wpBlueprintModal) -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR WÜEST + PANEDURO</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:800;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für Wüest + Paneduro</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie oben den Hero-Bereich, Ihre Kern-Methode («Innere Stärke entwickeln»), Ihre Gründer-Porträts, alle 9 Referenzlogos sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaltexten und Bildern ergänzt.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold-dark);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:800;color:var(--charcoal);" id="wpBpCategory">Themenbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Begleitung &amp; Umsetzung: Christine Wüest &amp; Nino Paneduro</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Barlow',sans-serif;font-size:0.8rem;font-weight:800;text-transform:uppercase;color:var(--charcoal);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Ausarbeitung aller Angebote (1:1 Führungskräfte-Coaching, 9 Levels Workshops, Reiss Profile, Hypnose &amp; MentalFitnessCenter)</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Übernahme aller 10 verifizierten Kundenstimmen, Praxis-Fallbeispiele, 11 Zertifizierungen &amp; Buch «Der Handball-Code»</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Persönliche Vorstellung von Christine Wüest &amp; Nino Paneduro sowie Ihrem Standort im Businesspark Sursee</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <button type="button" class="btn-cta btn-cta-gold btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Verstanden · Vorschau weiter ansehen</span>
        </button>
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
          <span>3-Schritte Smart-Anfrage testen</span>
        </a>
      </div>
    </div>
  </div>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""

def render_core_pillars_section(is_v2: bool = False) -> str:
    cta_href = "kontakt.html?thema=coaching" if is_v2 else "angebot.html"
    cta_label = "Thema im Erstgespräch besprechen" if is_v2 else "Säule & Methoden vertiefen"
    return f"""
  <!-- DIE METHODE: 4 SÄULEN FÜR INNERE STÄRKE & RESILIENZ -->
  <section id="methode" data-section="methode" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="methode_kicker">DIE METHODE · 4 SÄULEN FÜR NACHHALTIGE WIRKSAMKEIT</div>
        <h2 class="section-title" data-slot="methode_title">Innere Stärke entwickeln, systematisch auf vier Pfeilern aufgebaut.</h2>
        <p class="section-desc" data-slot="methode_desc">
          Als Mentoren, Coaches und Ratgeber begleiten wir Führungskräfte auf dem Weg zu innerer Stärke und Resilienz. Zuhörend und empathisch, aber auch klar und direkt sorgen wir in 1:1 Coachings, Workshops und Seminaren dafür, dass Sie souverän und selbstbewusst Ihre Zukunft sowie die Ihres Unternehmens gestalten.
        </p>
      </div>

      <div class="grid-2">
        <!-- Säule 1: Selbstführung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-selbstfuehrung.jpg" alt="Innere Stärke entwickeln mit Selbstführung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Säule 01 · Orientierung</span>
                <span class="icon-box">{SVG_COMPASS}</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Innere Stärke entwickeln mit Selbstführung</h3>
              <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:12px;">
                Wir unterstützen Sie als Mentoren und Ratgeber dabei, Ihre Fähigkeit zur Selbstführung weiterzuentwickeln. Denn erfolgreiche Führung basiert in erster Linie auf guter Selbstführung: Nur wer sich selbst klar führt, kann andere inspirierend führen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Schärfung der Selbstwahrnehmung und klare Priorisierung im Führungsalltag</span></div>
                <div class="check-item">{SVG_CHECK}<span>Neue Orientierung bei Wandel, wachsenden Ansprüchen und modernen Arbeitsformen</span></div>
              </div>
            </div>
            <a href="{cta_href}" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>{cta_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Säule 2: Stressmanagement -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-stressmanagement.jpg" alt="Innere Stärke mit dem richtigen Stressmanagement" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Säule 02 · Balance &amp; Energie</span>
                <span class="icon-box">{SVG_SHIELD}</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Innere Stärke mit dem richtigen Stressmanagement</h3>
              <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:12px;">
                Mit verschiedenen Ansätzen wie Achtsamkeit, Aktiv-Wach-Hypnose, Business-Hypnose oder gezielten Entspannungsübungen begegnen Sie dem Dauerstress mit neuer innerer Stärke und gewinnen Ihre mentale Regenerationsfähigkeit zurück.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Persönliche Stresstreiber aufdecken und aus der 70-Stunden-Spirale aussteigen</span></div>
                <div class="check-item">{SVG_CHECK}<span>Schnelle Erholung von Körper und Geist für überlegene Entscheidungsqualität</span></div>
              </div>
            </div>
            <a href="{cta_href}" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>{cta_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Säule 3: Selbstwirksamkeit -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-selbstwirksamkeit.jpg" alt="Innere Stärke durch Selbstwirksamkeit" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Säule 03 · Souveränität</span>
                <span class="icon-box">{SVG_ZAP}</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Innere Stärke durch Selbstwirksamkeit</h3>
              <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:12px;">
                Sie bewahren in unklaren Situationen einen kühlen Kopf, bewältigen Veränderungen, nehmen aktiv Einfluss und sind in der Lage, sich selbst und andere souverän zu führen, statt nur auf äusseren Druck zu reagieren.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Selbstzweifel überwinden und Vertrauen in die eigene Führungskompetenz stärken</span></div>
                <div class="check-item">{SVG_CHECK}<span>Vom Getriebensein zurück ins aktive, wirksame Gestalten kommen</span></div>
              </div>
            </div>
            <a href="{cta_href}" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>{cta_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Säule 4: Zukunftsgestaltung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-zukunftsplanung.jpg" alt="Innere Stärke wächst durch Zukunftsgestaltung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Säule 04 · Zukunft &amp; Vision</span>
                <span class="icon-box">{SVG_SPARKLES}</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Innere Stärke wächst durch Zukunftsgestaltung</h3>
              <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:12px;">
                Wir zeigen Ihnen, wie Sie ausserhalb Ihrer Komfortzone agieren und konkrete Schritte unternehmen, um die Zukunft für sich, Ihr Team und Ihr Unternehmen positiv zu gestalten und als Leader Stabilität zu vermitteln.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Klare Werte- &amp; Visionsarbeit mit dem 9 Levels Wertesystem und Reiss Profile</span></div>
                <div class="check-item">{SVG_CHECK}<span>Konkrete Umsetzungsschritte statt Fahren auf Sicht im Nebel</span></div>
              </div>
            </div>
            <a href="{cta_href}" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>{cta_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def render_founders_section(is_v2: bool = False) -> str:
    more_href = "kontakt.html?thema=erstgespraech" if is_v2 else "ueber-uns.html"
    more_label = "Persönliches Kennenlernen vereinbaren" if is_v2 else "Ausführliches Porträt & Werdegang lesen"
    return f"""
  <!-- WÜEST + PANEDURO GRÜNDER-VORSTELLUNG -->
  <section id="gruender" data-section="gruender" style="background-color:var(--bg-Warm);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="founders_kicker">WÜEST + PANEDURO · MENTOREN, COACHES &amp; RATGEBER</div>
        <h2 class="section-title" data-slot="founders_title">Wirtschaftspraxis auf Geschäftsleitungsebene trifft 25+ Jahre Spitzensport-Mentaltraining.</h2>
        <p class="section-desc" data-slot="founders_desc">
          Wir beraten und coachen Geschäftsführer, Führungskräfte und Unternehmen im Businesspark Sursee sowie schweizweit vor Ort und Online. Dabei verbinden wir fundierte Management-Erfahrung mit erprobten Methoden aus dem Hochleistungssport.
        </p>
      </div>

      <div class="grid-2">
        <!-- Christine Wüest -->
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-christine-wueest.jpg" alt="Christine Wüest – Expertin für Resilienz und innere Stärke" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Geschäftsführerin · Dipl. Mental Coach</span>
              <h3 style="font-size:1.5rem;font-weight:800;margin-bottom:6px;">Christine Wüest</h3>
              <p style="font-size:0.9rem;font-weight:700;color:var(--gold-dark);line-height:1.45;">
                «Christine Wüest verbindet Expertise mit Empathie und Klarheit mit Kompetenz.»
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div>
              <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:12px;">
                Sie ist ausgewiesene Expertin für Resilienz und innere Stärke. Nach ihrer Zeit bei der Swissair und dem Studium der Betriebswirtschaft war Christine Wüest über 10 Jahre in leitenden Positionen und in der Geschäftsleitung der IT-Branche sowie als Leiterin «Zentrale Dienste und HR» und Geschäftsleitungsmitglied in einem renommierten medizinischen Labor tätig.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Mehrjährige Geschäftsleitungs- &amp; HR-Verantwortung in IT und Labormedizin</span></div>
                <div class="check-item">{SVG_CHECK}<span>Spezialisiert auf Resilienz, Selbstführung, Fokus &amp; mentale Prüfungsvorbereitung</span></div>
              </div>
            </div>
            <a href="{more_href}" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>{more_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Nino Paneduro -->
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-nino-paneduro.jpg" alt="Nino Paneduro – Mentor und Ratgeber für innere Stärke" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Vorsitzender der GL · 4× Top 100 Trainer DACH</span>
              <h3 style="font-size:1.5rem;font-weight:800;margin-bottom:6px;">Nino Paneduro</h3>
              <p style="font-size:0.9rem;font-weight:700;color:var(--gold-dark);line-height:1.45;">
                «Nino Paneduro steht für Fokus, Konzentration, mentale Stärke und Klarheit.»
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div>
              <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:12px;">
                Seit über 25 Jahren trainiert und coacht Nino Paneduro Spitzensportler und Teams (Handball-Nationalspieler, Champions-League-Athleten, EM- und WM-Teilnehmer) und war zugleich über zwei Jahrzehnte in verschiedenen Führungspositionen im Zürcher Bankwesen tätig. Von 2021 bis 2024 wurde er viermal in Folge als «Top 100 Trainer &amp; Coaches DACH» (Performance) ausgezeichnet.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Zertifizierter 9 Levels Trainer, Reiss Motivation Profile Master &amp; CAS Sportpsychologie</span></div>
                <div class="check-item">{SVG_CHECK}<span>Dipl. Hypnosetherapeut (NGH/OHTC), HypnoSport- &amp; Aktiv-Wach-Hypnose-Spezialist</span></div>
              </div>
            </div>
            <a href="{more_href}" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>{more_label}</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>"""


V1_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light" data-slot="hero_kicker">WÜEST + PANEDURO · BUSINESSPARK SURSEE &amp; SCHWEIZWEIT</div>
          <h1 class="hero-title" data-slot="hero_title">
            Innere Stärke entwickeln – <span>Mit mehr Resilienz und Energie Ziele erreichen.</span>
          </h1>
          <p class="hero-lead" data-slot="hero_lead">
            Die täglichen Anforderungen als Führungskraft fordern Menschen extrem. Als Mentoren, Coaches und Ratgeber begleiten Christine Wüest und Nino Paneduro Führungskräfte, Teams und Unternehmen in 1:1 Coachings, Workshops und Impulsreferaten dabei, einen kühlen Kopf zu bewahren und die Zukunft souverän zu gestalten.
          </p>
          <div class="hero-actions">
            <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
              <span>Unverbindlichen Kennenlerntermin vereinbaren</span>
              {SVG_ARROW}
            </a>
            <a href="angebot.html" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
              <span>Angebot &amp; 4 Säulen entdecken</span>
            </a>
          </div>

          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val">25+ Jahre Erfahrung</span>
              <span class="hero-badge-lbl">Spitzensport-Mentaltraining &amp; Führungspraxis in Bankwesen, IT &amp; HR</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">4× Top 100 Trainer DACH</span>
              <span class="hero-badge-lbl">Ausgezeichnet durch Seminar.Inside in der Kategorie Performance</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">11 Zertifizierungen</span>
              <span class="hero-badge-lbl">9 Levels Wertesystem, Reiss Profile Master, CAS &amp; Business-Hypnose</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">Businesspark Sursee</span>
              <span class="hero-badge-lbl">Diskrete Coaching-Räume an der Allee 1b in Sursee sowie Inhouse &amp; Online</span>
            </div>
          </div>
        </div>

        <div class="hero-media-card">
          <img src="images/hero-wueest-paneduro.jpg" alt="Christine Wüest und Nino Paneduro – Innere Stärke entwickeln" data-slot="hero_image">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1rem;color:#181817;">Christine Wüest &amp; Nino Paneduro</div>
              <div style="font-size:0.8rem;color:var(--crimson);font-weight:700;">Mentoren, Coaches &amp; Ratgeber · Businesspark Sursee</div>
            </div>
            <a href="ueber-uns.html" class="btn-cta btn-cta-outline-light btn-sm">
              <span>Über uns</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE HERAUSFORDERUNG IM FÜHRUNGSALLTAG (DANIEL & SABINE) -->
  <section data-section="herausforderung" style="background-color:var(--bg-Warm);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="challenge_kicker">DIE HERAUSFORDERUNG IM FÜHRUNGSALLTAG</div>
        <h2 class="section-title" data-slot="challenge_title">Sind Sie Führungskraft? Dann kommen Ihnen die Geschichten von Daniel und Sabine wahrscheinlich bekannt vor.</h2>
        <p class="section-desc" data-slot="challenge_desc">
          Daniel leitet die Abteilung eines mittelständischen Unternehmens und muss sich um gefühlt 1'000 Dinge gleichzeitig kümmern. Trotz der langen Arbeitstage reicht die Zeit nicht aus, um allen und allem gerecht zu werden, die Energie schwindet und der Druck wirkt sich bis ins Privatleben aus. Seine Kollegin Sabine möchte als Führungskraft weiterkommen und selbstsicherer auftreten, kämpft jedoch mit Selbstzweifeln und Dauerstress.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge" style="background-color:var(--crimson-soft);color:var(--crimson);border-color:#F5B7C1;">Status Quo unter Hochdruck</span>
              <span class="icon-box" style="background-color:var(--crimson);color:#FFFFFF;">{SVG_ZAP}</span>
            </div>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Typische Warnsignale im heutigen Management</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Viele Führungskräfte und Unternehmer stehen heute vor denselben strukturellen und persönlichen Belastungsproben:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Dauerstress &amp; 70-Stunden-Wochen:</strong> Sie erleben mehr Stress und Erwartungsdruck von allen Seiten als je zuvor.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Reagieren statt Agieren:</strong> Im Minutentakt treffen E-Mails und dringende Anfragen ein, für strategische Führung fehlt der Freiraum.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Gefühl der Fremdsteuerung:</strong> Sie fühlen sich als Getriebener im eigenen Hamsterrad und können abends kaum noch abschalten.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Fahren auf Sicht:</strong> Sie müssen in einer unsicheren Zukunft planen und Ihrem Team gleichzeitig Orientierung geben.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=erstgespraech" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Standortbestimmung im Erstgespräch anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Der Schlüssel: Innere Stärke</span>
              <span class="icon-box" style="background-color:var(--gold);color:#161615;">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Die Zukunft resilient, souverän und selbstbewusst gestalten</h3>
            <p style="font-size:0.92rem;color:#E5E7EB;margin-bottom:14px;">
              Menschen mit innerer Stärke und Resilienz sehen das Leben optimistisch. Sie gestalten selbstwirksam und mit Selbstvertrauen ihr berufliches und privates Leben:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Klarer Kopf unter Hochdruck:</strong> Sie bewahren auch in unübersichtlichen Situationen Ruhe, Fokus und Entscheidungsstärke.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Bewusster Umgang mit Energie:</strong> Durch Mentaltraining, Achtsamkeit und Business-Hypnose regenerieren Körper und Geist spürbar schneller.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Wertebasierter Führungsstil:</strong> Sie kennen Ihre Lebensmotive (Reiss Profile) und Werte (9 Levels) und führen authentisch.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Vom Reagieren ins Gestalten:</strong> Sie gehen als Leader mutig, inspirierend und ausgeglichen voran.</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Jetzt unverbindlichen Kennenlerntermin vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

{render_core_pillars_section(is_v2=False)}

  <!-- ÜBERBLICK ÜBER DAS ANGEBOT (4 FORMATE) -->
  <section id="angebot-ueberblick" data-section="angebot-ueberblick" style="background-color:var(--charcoal-deep);color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker kicker-light" data-slot="offer_kicker">ANGEBOT &amp; FORMATE · MASSGESCHNEIDERT FÜR SIE UND IHR TEAM</div>
        <h2 class="section-title" style="color:#FFFFFF;" data-slot="offer_title">Wie wir Führungskräfte, Teams und Unternehmen begleiten.</h2>
        <p class="section-desc" style="color:#D1D5DB;" data-slot="offer_desc">
          Ob vertrauliches 1:1 Sparring im Businesspark Sursee, intensiver Führungs-Workshop mit Ihrem Kader oder inspirierende Keynote an Ihrer Jahrestagung: Wir passen unseren Methodenkoffer präzise auf Ihre Ausgangslage an.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Format 01 · 1:1 Sparring</span>
              <span class="icon-box" style="background-color:var(--gold);color:#161615;">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">Führungskräfte- &amp; Einzel-Coaching</h3>
            <p style="font-size:0.9rem;color:#D1D5DB;margin-bottom:12px;">
              Individuelle Standortbestimmung und Begleitung für Geschäftsführer, Führungskräfte, Selbstständige und Spitzensportler, im Businesspark Sursee oder Online.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Persönliche Werte- &amp; Motiv-Analyse (9 Levels &amp; Reiss Motivation Profile)</span></div>
              <div class="check-item">{SVG_CHECK}<span>Mentale Fokussierung, Stressabbau &amp; Aktiv-Wach- / Business-Hypnose</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>1:1 Coaching anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Format 02 · Unternehmen &amp; Kader</span>
              <span class="icon-box" style="background-color:var(--gold);color:#161615;">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">Team-Trainings &amp; Firmen-Workshops</h3>
            <p style="font-size:0.9rem;color:#D1D5DB;margin-bottom:12px;">
              Praxisnahe Halbtages-, Tages- und 2-Tages-Workshops (wie der bewährte «TUNE IN» Workshop oder 9 Levels Führungs-Workshops) für Abteilungen, KMU und Verwaltungen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Sofort anwendbare Mental-Tools für Fokus und Leichtigkeit im Daily Business</span></div>
              <div class="check-item">{SVG_CHECK}<span>Gemeinsames Werteverständnis und gelebte Resilienz im gesamten Führungsteam</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Firmen-Workshop anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Format 03 · Events &amp; Buch</span>
              <span class="icon-box" style="background-color:var(--gold);color:#161615;">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">Impulsreferate, Keynotes &amp; «Der Handball-Code»</h3>
            <p style="font-size:0.9rem;color:#D1D5DB;margin-bottom:12px;">
              Packende Keynotes über die Parallelen zwischen Spitzensport und Management sowie unser 2025 erschienenes Buch «Der Handball-Code – Was, wenn mentale Stärke der wahre Gamechanger ist?».
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>12 echte Geschichten aus Nati und Bundesliga übertragen auf Führung &amp; Business</span></div>
              <div class="check-item">{SVG_CHECK}<span>Ideal für Kaderanlässe, Kick-offs, Kundenevents und Verbandstagungen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=keynote" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Keynote / Impulsreferat anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Format 04 · Dranbleiben im Alltag</span>
              <span class="icon-box" style="background-color:var(--gold);color:#161615;">{SVG_SPARKLES}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">MentalFitnessCenter &amp; Jahres-Begleitung</h3>
            <p style="font-size:0.9rem;color:#D1D5DB;margin-bottom:12px;">
              Mentale Stärke entsteht nicht an einem einzigen Tag, sondern durch regelmässiges Training und feste Routinen im Alltag.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Inner Strength Circle:</strong> Das Jahresprogramm für nachhaltige mentale Stärke</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>45 Minuten über Mittag</strong> (monatlicher Live-Call) &amp; <strong>33 Daily Lunch Bites</strong></span></div>
            </div>
          </div>
          <a href="angebot.html#mentalfitnesscenter" class="btn-cta btn-cta-outline-light btn-sm" style="width:100%;">
            <span>Programme im Detail ansehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

{render_founders_section(is_v2=False)}

  <!-- ORIGINAL-REFERENZLOGOS & AUSGEWÄHLTE KUNDENSTIMMEN -->
  <section id="referenzlogos" data-section="referenzlogos" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="ref_kicker">REFERENZEN &amp; KUNDENSTIMMEN · VERTRAUEN AUS WIRTSCHAFT, VERWALTUNG &amp; SPORT</div>
        <h2 class="section-title" data-slot="ref_title">Unternehmen, Verbände und Führungskräfte, die auf Wüest + Paneduro zählen.</h2>
        <p class="section-desc" data-slot="ref_desc">
          Von kantonalen Amtsstellen über mittelständische KMU und Gesundheitsbetriebe bis hin zu nationalen Sportverbänden und Spitzensportlern: Unsere Klientinnen und Klienten schätzen die Verbindung aus Empathie, Klarheit und unmittelbarer Praxistauglichkeit.
        </p>
      </div>

      {render_reference_logos_grid()}

      <div style="margin-top:52px;">
        <h3 style="font-size:1.55rem;font-weight:800;margin-bottom:22px;">Ausgewählte Stimmen unserer Klientinnen und Klienten</h3>
        {render_testimonials_grid(limit=4)}
      </div>

      <div style="margin-top:32px;display:flex;justify-content:center;">
        <a href="referenzen.html" class="btn-cta btn-cta-primary">
          <span>Alle 10 Original-Kundenstimmen &amp; Praxis-Berichte lesen</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </section>

  <!-- DIREKT-CTA BANNER -->
  <section data-section="cta-banner" style="background-color:var(--charcoal-deep);color:#FFFFFF;padding:64px 0;">
    <div class="container">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:28px;flex-wrap:wrap;background-color:var(--charcoal);border:2px solid var(--gold);border-radius:var(--radius-md);padding:32px 34px;">
        <div style="max-width:680px;">
          <div class="section-kicker kicker-light">GEHEN SIE JETZT DEN ERSTEN SCHRITT</div>
          <h2 style="font-size:clamp(1.65rem,2.7vw,2.25rem);font-weight:800;color:#FFFFFF;margin-bottom:10px;">
            Vereinbaren Sie jetzt einen unverbindlichen Kennenlerntermin!
          </h2>
          <p style="font-size:0.96rem;color:#E5E7EB;">
            Im Businesspark Sursee (Allee 1b, CH-6210 Sursee), direkt bei Ihnen im Unternehmen oder unkompliziert per Video-Call. In 3 kurzen Schritten erstellen Sie Ihre Anfrage inklusive persönlichem 1-Seiten-PDF-Dossier.
          </p>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:12px;">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>3-Schritte Smart-Anfrage starten</span>
            {SVG_ARROW}
          </a>
          <a href="tel:+41786062056" class="btn-cta btn-cta-outline-light">
            {SVG_PHONE}
            <span>+41 78 606 20 56</span>
          </a>
        </div>
      </div>
    </div>
  </section>
"""


V1_ANGEBOT_BODY = f"""
  <!-- HERO ANGEBOT -->
  <section class="hero-section" data-section="hero-angebot" style="padding:60px 0 70px;">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light">ANGEBOT, PROGRAMME &amp; METHODEN · WÜEST + PANEDURO</div>
          <h1 class="hero-title">
            Massgeschneiderte Begleitung für <span>Führungskräfte, Teams und Unternehmen.</span>
          </h1>
          <p class="hero-lead">
            Wir bedienen uns eines grossen Koffers an wissenschaftlich fundierten und praxiserprobten Methoden, die wir präzise auf den jeweiligen Menschen und die Situation anpassen, vom 1:1 Executive-Coaching über 9 Levels Team-Workshops bis zu Business-Hypnose und dem MentalFitnessCenter.
          </p>
          <div class="hero-actions">
            <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-gold">
              <span>Passendes Format anfragen</span>
              {SVG_ARROW}
            </a>
            <a href="#vier-saeulen-detail" class="btn-cta btn-cta-outline-light">
              <span>Zu den 4 Säulen im Detail</span>
            </a>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/header-selbstfuehrung.jpg" alt="Angebot und Coaching Wüest + Paneduro">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1rem;color:#181817;">Praxisnah, empathisch &amp; konsequent</div>
              <div style="font-size:0.8rem;color:var(--crimson);font-weight:700;">Businesspark Sursee · Inhouse in Ihrer Firma · Online</div>
            </div>
            <span class="top-bar-badge">11 Zertifizierungen</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 4 KOOPERATIONS-FORMATE IM DETAIL -->
  <section id="programme" data-section="programme" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">UNSERE 4 KERNFORMATE FÜR BUSINESS &amp; SPITZENSPORT</div>
        <h2 class="section-title">Vom individuellen 1:1 Sparring bis zur nachhaltigen Team-Entwicklung.</h2>
        <p class="section-desc">
          Wählen Sie das Format, das optimal zu Ihrer aktuellen Herausforderung passt, oder kombinieren Sie Einzel-Coaching und Team-Workshop für maximale Umsetzungskraft im Führungsalltag.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">01 · Individuelles Executive-Sparring</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">1:1 Führungskräfte- &amp; Einzel-Coaching</h3>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:14px;">
              Vertrauliche Zusammenarbeit auf Augenhöhe für Geschäftsführer, Abteilungsleitende, Selbstständige und Leistungsträger. Gemeinsam räumen wir Hindernisse aus dem Weg, schärfen Ihren Führungsstil und stärken Ihre persönliche Resilienz.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Standortbestimmung &amp; Werte-Klarheit:</strong> Auswertung mit dem 9 Levels Wertesystem oder Reiss Motivation Profile (RMP).</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Fokus unter Prüfungs- &amp; Entscheidungsdruck:</strong> Punktgenaues Abrufen der Bestleistung (bewährt bei eidg. Prüfungen und im Spitzensport).</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Durchführungsort:</strong> Diskret im Businesspark Sursee (Allee 1b) oder ortsunabhängig per Video-Call.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>1:1 Coaching im 3-Schritte-Assistenten wählen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">02 · Kader &amp; Organisationen</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">Unternehmens-Workshops &amp; Team-Trainings</h3>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:14px;">
              Interaktive Halbtages-, Tages- und 2-Tages-Workshops für Führungsteams, Geschäftsleitungen und ganze Abteilungen, unter anderem bekannt durch unseren «TUNE IN» Workshop und unsere 9-Levels-Kaderseminare.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>9 Levels Team-Profil:</strong> Wie persönliche und organisationale Werte den Führungsstil und die Zusammenarbeit prägen.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>TUNE IN Mental-Tools:</strong> Leicht anwendbare Werkzeuge für Fokus, Gelassenheit und gesunde Abgrenzung im Daily Business.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Nachhaltiger Transfer:</strong> Konkrete Leitplanken statt kurzlebiger Seminar-Euphorie.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Team-Workshop im 3-Schritte-Assistenten wählen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top" id="handball-code">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">03 · Inspiration &amp; Publikation</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">Impulsreferate, Keynotes &amp; Buch «Der Handball-Code»</h3>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:14px;">
              Was trennt Gewinner von denen, die unter Druck einbrechen? In unseren Impulsreferaten und unserem Buch «Der Handball-Code» (erschienen im Juli 2025) schlagen wir die Brücke zwischen 15+ Jahren Spitzensport und moderner Unternehmensführung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Der Kopf entscheidet:</strong> Wie Führungskräfte und Teams mit Rückschlägen, Veränderungsdruck und hohen Erwartungen umgehen.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>12 echte Athleten-Geschichten:</strong> Direkt aus der Schweizer Nationalmannschaft und der Bundesliga übersetzt in den Führungsalltag.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Massgeschneiderte Dauer:</strong> 30 bis 90 Minuten inkl. Q&amp;A für Kadersitzungen, Kundenanlässe und Kongresse.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=keynote" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Impulsreferat / Keynote anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top" id="mentalfitnesscenter">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">04 · Kontinuierliche Begleitung</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">MentalFitnessCenter: Circle, Live-Calls &amp; Lunch Bites</h3>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:14px;">
              Ein einzelner Workshop pro Jahr verändert noch keine tief verankerten Gewohnheiten. Unser MentalFitnessCenter begleitet Sie kontinuierlich durch das ganze Jahr:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Inner Strength Circle:</strong> Der Jahrescircle zur nachhaltigen Verankerung neuer mentaler Routinen im Alltag.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>45 Minuten über Mittag:</strong> Monatlicher Live-Call (jeweils am letzten Donnerstag im Monat, 12:30–13:15 Uhr) zu Fokus &amp; Resilienz.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>33 Daily Lunch Bites:</strong> 33 Tage lang täglich kompakte, sofort umsetzbare Impulse für Ihre innere Stärke.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=erstgespraech" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Teilnahme &amp; Details anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 4 VERTIEFUNGS-SÄULEN IM VOLLEN ORIGINAL-WORTLAUT -->
  <section id="vier-saeulen-detail" data-section="vier-saeulen-detail" style="background-color:var(--bg-Warm);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">VERTIEFUNG DER 4 THEMENFELDER · 100 % ORIGINAL-KONZEPT</div>
        <h2 class="section-title">Die vier Entwicklungsfelder für Führungskräfte im Detail.</h2>
        <p class="section-desc">
          Jede Führungspersönlichkeit und jedes Unternehmen steht an einem anderen Punkt. Hier sehen Sie im Detail, welche Fragestellungen wir in den vier Kernsäulen gemeinsam bearbeiten.
        </p>
      </div>

      <div class="grid-2">
        <!-- Detail 1: Selbstführung -->
        <div class="content-card" id="selbstfuehrung">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Themenfeld 1 · Selbstführung</span>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Innere Stärke erlangen mit Selbstführung</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Die Arbeitswelt ist in ständigem Wandel, komplex und dynamisch, traditionelle Führungsmethoden sowie reines Zeitmanagement reichen oft nicht mehr aus. Auf dem Schreibtisch stapeln sich die Unterlagen, im Minutentakt kommen neue E-Mails an und ein Termin jagt den nächsten.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              <strong>Erfolgreiche Führung braucht Selbstführung:</strong> Wer die Kompetenz hat, sich selbst zu führen, nutzt die zur Verfügung stehende Zeit besser, priorisiert klarer und beachtet die eigenen Bedürfnisse. In unserer Zusammenarbeit schärfen wir Ihre Selbstwahrnehmung und richten Ihre Selbstführung passend zu Ihrer Rolle neu aus.
            </p>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-outline btn-sm">
            <span>Selbstführung optimieren</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- Detail 2: Stressmanagement -->
        <div class="content-card" id="stressmanagement">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Themenfeld 2 · Stressmanagement</span>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Balance statt Dauerstress im Führungsalltag</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              70-Stunden-Wochen sind für viele Führungskräfte keine Ausnahme: Grosse Projekte, wichtige Kunden, knappe Deadlines, und zuhause wartet die Familie. Hält der Stress über Monate oder Jahre an, führt die Daueranspannung zu Erschöpfung und übereilten Entscheidungen.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              <strong>Persönlicher Umgang mit Stress:</strong> Gemeinsam im Coaching decken wir Ihre individuellen Stresstreiber auf und erarbeiten eine Strategie, wie Sie neue Energie gewinnen. Mit Achtsamkeit, Aktiv-Wach-Hypnose, Business-Hypnose und Entspannungsübungen reflektieren Sie sich besser und finden zurück in Ihre Kraft.
            </p>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-outline btn-sm">
            <span>Stressmanagement-Strategie besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- Detail 3: Selbstwirksamkeit -->
        <div class="content-card" id="selbstwirksamkeit">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Themenfeld 3 · Selbstwirksamkeit</span>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Selbstwirksamkeit, eine essenzielle Führungskompetenz</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Auf dem Markt und im Unternehmen herrscht grosser Veränderungsdruck, dazu kommt der Erwartungsdruck von «oben» sowie von den Mitarbeitenden. Fehlt es in herausfordernden Phasen an Selbstwirksamkeit, entstehen Selbstzweifel und das Gefühl, nur noch getrieben zu sein.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              <strong>Selbstwirksamkeit gezielt trainieren:</strong> Selbstwirksame Menschen lösen Aufgaben mit Um- und Weitsicht, bewahren in unklaren Situationen einen kühlen Kopf und nutzen Veränderungen als Chance für persönliches und unternehmerisches Wachstum.
            </p>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-outline btn-sm">
            <span>Selbstwirksamkeit trainieren</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- Detail 4: Zukunftsplanung -->
        <div class="content-card" id="zukunftsplanung">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Themenfeld 4 · Zukunftsplanung &amp; Zukunftsgestaltung</span>
            <h3 style="font-size:1.35rem;font-weight:800;margin-bottom:10px;">Souverän als Zukunftsgestalter vorangehen</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Führungskräfte bewegen sich im Spannungsfeld zwischen Sicherheit und Risiko, zwischen Zukunft und Tradition. Gerade wenn vieles im Nebel liegt, brauchen Mitarbeitende Leader, die mutig vorangehen und nicht in veralteten Schablonen denken.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              <strong>Vom Reden ins konkrete Handeln:</strong> Wir klären mit Ihnen Ihre Vision für die kommenden Jahre und zeigen Ihnen, wie Sie ausserhalb Ihrer Komfortzone konkrete Schritte unternehmen, die Stabilität und Zuversicht auf Ihr gesamtes Umfeld übertragen.
            </p>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-outline btn-sm">
            <span>Zukunftsstrategie angehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- BUCH & METHODEN-SPOTLIGHT -->
  <section data-section="methoden-spotlight" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="grid-2">
        <div class="content-card">
          <div style="display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:start;">
            <img src="images/buch-der-handball-code.jpg" alt="Buch Der Handball-Code von Nino Paneduro und Christine Wüest" style="width:100%;border-radius:4px;border:1px solid var(--border-light);" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Buch-Publikation 2025</span>
              <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">«Der Handball-Code» – Was, wenn mentale Stärke der wahre Gamechanger ist?</h3>
              <p style="font-size:0.9rem;color:var(--text-body);">
                Basierend auf über 15 Jahren intensiver Arbeit im Spitzensport zeigen Christine Wüest und Nino Paneduro anhand von 12 echten Geschichten aus der Nationalmannschaft und Bundesliga, warum am Ende der Kopf über Sieg oder Niederlage entscheidet, im Spiel, im Business und im Leben.
              </p>
            </div>
          </div>
          <a href="kontakt.html?thema=keynote" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Buch-Impuls oder Keynote anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card">
          <div style="display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:start;">
            <img src="images/award-top100-trainer.jpg" alt="Top 100 Trainer und Coaches DACH Auszeichnung Seminar.Inside" style="width:100%;border-radius:4px;border:1px solid var(--border-light);" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Ausgezeichnete Methodenkompetenz</span>
              <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:8px;">9 Levels, Reiss Motivation Profile &amp; Business-Hypnose</h3>
              <p style="font-size:0.9rem;color:var(--text-body);">
                Wir verbinden analytische Diagnostik (9 Levels of Value Systems für Personen &amp; Teams sowie Reiss Motivation Profile für die 16 Lebensmotive) mit tiefgreifender mentaler Arbeit durch Aktiv-Wach-Hypnose und Business-Hypnose zur schnellen Regeneration und Blockadenlösung.
              </p>
            </div>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Methoden im Kennenlerngespräch erleben</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""


V1_UEBER_UNS_BODY = f"""
  <!-- HERO ÜBER UNS -->
  <section class="hero-section" data-section="hero-ueber-uns" style="padding:60px 0 70px;">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light">ÜBER UNS · MENTOREN, COACHES &amp; RATGEBER</div>
          <h1 class="hero-title">
            Christine Wüest und Nino Paneduro – <span>Perspektiven und Wege für eine erfolgreiche Zukunft.</span>
          </h1>
          <p class="hero-lead">
            Als Mentoren, Coaches und Ratgeber ist es uns wichtig, dass das Thema innere Stärke im Business-Alltag fest etabliert wird. Mit Expertise, Kreativität und Offenheit begegnen wir Ihren Herausforderungen im Businesspark Sursee und schweizweit vor Ort.
          </p>
          <div class="hero-actions">
            <a href="kontakt.html?thema=erstgespraech" class="btn-cta btn-cta-gold">
              <span>Persönliches Gespräch vereinbaren</span>
              {SVG_ARROW}
            </a>
            <a href="#zertifizierungen" class="btn-cta btn-cta-outline-light">
              <span>Alle 11 Aus- &amp; Weiterbildungen</span>
            </a>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/header-mentoren-duo.jpg" alt="Christine Wüest und Nino Paneduro im Businesspark Sursee">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1rem;color:#181817;">Unser Ziel: Menschen zu innerer Stärke führen</div>
              <div style="font-size:0.8rem;color:var(--crimson);font-weight:700;">Nino Paneduro GmbH · Businesspark Sursee</div>
            </div>
            <span class="top-bar-badge">Sursee &amp; Schweizweit</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- AUSFÜHRLICHE PORTRÄTS CHRISTINE WÜEST & NINO PANEDURO -->
  <section data-section="portraets-detail" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">UNSERE GESCHICHTE &amp; KOMPETENZ</div>
        <h2 class="section-title">Zwei Persönlichkeiten, ein gemeinsamer Anspruch an echte Wirksamkeit.</h2>
        <p class="section-desc">
          Wir kennen den Führungsdruck nicht aus Lehrbüchern, sondern aus jahrzehntelanger eigener Führungsverantwortung in der Wirtschaft sowie aus der mentalen Begleitung im internationalen Spitzensport.
        </p>
      </div>

      <div class="grid-2">
        <!-- Christine Wüest Ausführlich -->
        <div class="content-card card-accent-top">
          <div>
            <img src="images/header-christine-wueest.jpg" alt="Christine Wüest – Expertin für Resilienz und innere Stärke" style="width:100%;height:230px;object-fit:cover;border-radius:var(--radius-sm);margin-bottom:18px;" loading="lazy" decoding="async">
            <span class="meta-badge" style="margin-bottom:8px;">Christine Wüest Paneduro · Geschäftsführerin</span>
            <h3 style="font-size:1.45rem;font-weight:800;margin-bottom:10px;">Christine Wüest, Klar und zuverlässig zum Ziel</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Christine Wüest verbindet Expertise mit Empathie und Klarheit mit Kompetenz. Ihre erste prägende Begegnung mit innerer Stärke hatte sie während ihrer Tätigkeit als Flight-Attendant bei der <strong>Swissair</strong>: «Dort war ich mit vielen unterschiedlichen Lebensrealitäten konfrontiert und fasziniert davon, wie Menschen mit innerer und mentaler Stärke teils enorme Herausforderungen meisterten.»
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Nach dem <strong>Studium der Betriebswirtschaft</strong> führte ihr beruflicher Weg in die <strong>IT-Branche</strong>, in der sie mehr als 10 Jahre in leitenden Positionen und in der Geschäftsleitung tätig war. Es folgten weitere Jahre in einem renommierten medizinischen Labor (Bioanalytica) als <strong>Leiterin «Zentrale Dienste und HR» sowie in der Geschäftsleitung</strong>.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Als <strong>Dipl. Mental Coach</strong> steht Christine Wüest ihren Klientinnen und Klienten als klarer und zuverlässiger Ratgeber zur Seite, damit Hindernisse aus dem Weg geräumt werden und Führungskräfte ihre Zukunft selbstbestimmt, kraftvoll und souverän gestalten.
            </p>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Coaching bei Christine Wüest anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- Nino Paneduro Ausführlich -->
        <div class="content-card card-accent-top">
          <div>
            <img src="images/header-nino-paneduro.jpg" alt="Nino Paneduro – Mentor und Ratgeber für innere Stärke" style="width:100%;height:230px;object-fit:cover;border-radius:var(--radius-sm);margin-bottom:18px;" loading="lazy" decoding="async">
            <span class="meta-badge" style="margin-bottom:8px;">Antonino Paneduro · Vorsitzender der Geschäftsführung</span>
            <h3 style="font-size:1.45rem;font-weight:800;margin-bottom:10px;">Nino Paneduro – Wertschätzend zu langfristiger Erfolgssicherung</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Nino Paneduro steht für Fokus, Konzentration, mentale Stärke und Klarheit. Seit <strong>mehr als 25 Jahren</strong> trainiert, coacht und berät er Spitzensportler und Mannschaften, darunter Handballnationalspieler, Champions-League-Handballer sowie EM- und WM-Teilnehmer aus verschiedenen Sportarten, auch beim mentalen und emotionalen Comeback nach schweren Verletzungen.
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Im Businessleben verfügt er über einen ebenso breiten Erfahrungsschatz: <strong>Mehr als zwei Jahrzehnte war er im Zürcher Bankwesen in verschiedenen Führungspositionen</strong> tätig. «Häufig weisen die Themen einer Führungsperson direkte Parallelen zu denen von Spitzensportlern auf, etwa beim Leistungsdruck, beim Visionen-Umsetzen oder beim Abrufen von Höchstleistung.»
            </p>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Nino Paneduro wurde von 2021 bis 2024 <strong>viermal in Folge als «Top 100 Trainer &amp; Coaches in der DACH-Region»</strong> (Rubrik Performance, Seminar.Inside) ausgezeichnet.
            </p>
          </div>
          <a href="kontakt.html?thema=coaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Coaching bei Nino Paneduro anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 11 AUS- UND WEITERBILDUNGEN / ZERTIFIZIERUNGEN -->
  <section id="zertifizierungen" data-section="zertifizierungen" style="background-color:var(--bg-Warm);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">QUALIFIKATIONEN &amp; ZERTIFIZIERUNGEN</div>
        <h2 class="section-title">Unsere 11 Aus- und Weiterbildungen im Überblick.</h2>
        <p class="section-desc">
          Fundierte Methodik statt oberflächlicher Motivationssprüche: Unsere Begleitung stützt sich auf anerkannte Abschlüsse in Coaching, Sportpsychologie, Wertediagnostik und Hypnosetherapie.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Coaching &amp; Management</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:10px;">Business-Coaching, Werte- &amp; Motivdiagnostik</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. Coach Swiss Coaching Association (SCA)</strong></span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Zertifizierter 9 Levels Trainer</strong> (Wertesystem-Analyse für Führungskräfte, Teams &amp; Organisationen)</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Reiss Motivation Profile (RMP) Master</strong> (Wissenschaftliche Analyse der 16 Lebensmotive)</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. Kaufmann KFS</strong> &amp; Betriebswirtschaftliche Geschäftsleitungspraxis</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>4× Top 100 Trainer &amp; Coach DACH</strong> (Seminar.Inside, Rubrik Performance, 2021–2024)</span></div>
            </div>
          </div>
          <a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm">
            <span>Ergebnisse in den Kundenstimmen lesen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Mentaltraining &amp; Hypnose</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:10px;">Spitzensport-Psychologie &amp; Moderne Hypnose</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Certificate of Advanced Studies (CAS)</strong> in psychologischem und mentalem Training im Sport</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. Mentalcoach</strong> &amp; <strong>Dipl. Mentaltrainer</strong></span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. Hypnosetherapeut</strong> (NGH National Guild of Hypnotists USA &amp; Omni Hypnosis Training Center OHTC)</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. Aktiv-Wach-Hypnose-Coach</strong></span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Dipl. HypnoSport-Experte</strong> &amp; <strong>Dipl. HypnoPerform-Spezialist</strong></span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm">
            <span>Methoden-Frage stellen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- STANDORT BUSINESSPARK SURSEE -->
  <section data-section="standort-sursee" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="section-kicker">STANDORT ZENTRALSCHWEIZ &amp; SCHWEIZWEIT</div>
            <h3 style="font-size:1.45rem;font-weight:800;margin-bottom:10px;">Businesspark Sursee – Allee 1b, CH-6210 Sursee</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Unsere Coaching- und Trainingsräumlichkeiten im modernen Businesspark Sursee bieten eine ruhige, diskrete und inspirierende Atmosphäre, ideal gelegen zwischen Luzern, Aarau, Zug, Basel und Zürich (unmittelbar beim Bahnhof Sursee und Autobahnausfahrt A2).
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Vor Ort in Sursee:</strong> 1:1 Executive-Coachings, Hypnose-Sitzungen und Kleingruppen-Sparrings an der Allee 1b.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Inhouse &amp; Klausur-Orte:</strong> Team-Workshops direkt in Ihrem Unternehmen oder in Seminarhotels (z. B. Herzberg Uffikon, Aarau, Zentralschweiz).</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Online &amp; Hybrid:</strong> Ortsunabhängiges Coaching und Live-Calls über Mittag.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=erstgespraech" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Termin im Businesspark Sursee oder Online buchen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card" style="padding:0;overflow:hidden;">
          <img src="images/header-kontakt.jpg" alt="Kontakt und Standort Businesspark Sursee Wüest + Paneduro" style="width:100%;height:260px;object-fit:cover;" loading="lazy" decoding="async">
          <div style="padding:22px 26px;">
            <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.15rem;color:var(--charcoal);margin-bottom:6px;">
              Nino Paneduro GmbH · Wüest + Paneduro
            </div>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:10px;">
              Businesspark Sursee · Allee 1b · CH-6210 Sursee<br>
              Telefon: <strong>+41 78 606 20 56</strong> / +41 79 468 21 46<br>
              E-Mail: <strong>mail@innere-staerke.business</strong> · UID: CHE-279.321.936 MWST
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""


V1_REFERENZEN_BODY = f"""
  <!-- HERO REFERENZEN -->
  <section class="hero-section" data-section="hero-referenzen" style="padding:60px 0 70px;">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light">REFERENZEN &amp; KUNDENSTIMMEN · WÜEST + PANEDURO</div>
          <h1 class="hero-title">
            Das sagen Kunden über die Zusammenarbeit mit <span>Christine Wüest &amp; Nino Paneduro.</span>
          </h1>
          <p class="hero-lead">
            Echte Rückmeldungen von Führungskräften, Unternehmerinnen, kantonalen Bereichsleitenden, ICT-Spezialisten und Spitzensportlern: Lesen Sie hier alle 10 Original-Kundenstimmen und sehen Sie unsere Referenz-Unternehmen im Überblick.
          </p>
          <div class="hero-actions">
            <a href="kontakt.html" class="btn-cta btn-cta-gold">
              <span>Eigenes Anliegen besprechen</span>
              {SVG_ARROW}
            </a>
            <a href="#alle-kundenstimmen" class="btn-cta btn-cta-outline-light">
              <span>Direkt zu allen 10 Kundenstimmen</span>
            </a>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/header-kundenstimmen.jpg" alt="Kundenstimmen und Referenzen Wüest + Paneduro">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1rem;color:#181817;">9 Referenz-Logos &amp; 10 ausführliche Stimmen</div>
              <div style="font-size:0.8rem;color:var(--crimson);font-weight:700;">Wirtschaft · Öffentliche Verwaltung · Gesundheitswesen · Spitzensport</div>
            </div>
            <span class="top-bar-badge">100 % Original-Feedback</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 9 REFERENZ-UNTERNEHMEN MIT LOGOS -->
  <section data-section="referenz-unternehmen" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">UNSERE REFERENZ-UNTERNEHMEN &amp; ORGANISATIONEN</div>
        <h2 class="section-title">Branchenübergreifendes Vertrauen in der Deutschschweiz.</h2>
        <p class="section-desc">
          Ob kantonale Verwaltung, Versicherungs- und Finanzwirtschaft, medizinische Labordiagnostik, Detailhandel oder nationaler Sportverband: Innere Stärke ist in jeder Branche der entscheidende Erfolgsfaktor.
        </p>
      </div>

      {render_reference_logos_grid()}
    </div>
  </section>

  <!-- ALLE 10 ORIGINAL-KUNDENSTIMMEN IM VOLLEN WORTLAUT -->
  <section id="alle-kundenstimmen" data-section="alle-kundenstimmen" style="background-color:var(--bg-Warm);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ALLE 10 VERIFIZIERTEN KUNDENSTIMMEN · UNGEKÜRZTER ORIGINALWORTLAUT</div>
        <h2 class="section-title">Wie sich innere Stärke im Führungs-, Berufs- und Sportalltag auswirkt.</h2>
        <p class="section-desc">
          Vom 9 Levels Führungs-Workshop beim Kanton Aargau über den TUNE IN Workshop und das Reiss Motivation Profile bis hin zu 10+ Jahren Mentalcoaching im Spitzenhandball:
        </p>
      </div>

      {render_testimonials_grid(limit=10)}
    </div>
  </section>
"""


V2_INDEX_BODY = f"""
  <!-- HERO SECTION (ZEIGEVERSION: KOMPLETT AUSGEARBEITET) -->
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light" data-slot="hero_kicker">WÜEST + PANEDURO · BUSINESSPARK SURSEE &amp; SCHWEIZWEIT</div>
          <h1 class="hero-title" data-slot="hero_title">
            Innere Stärke entwickeln – <span>Mit mehr Resilienz und Energie Ziele erreichen.</span>
          </h1>
          <p class="hero-lead" data-slot="hero_lead">
            Die täglichen Anforderungen als Führungskraft fordern Menschen extrem. Als Mentoren, Coaches und Ratgeber begleiten Christine Wüest und Nino Paneduro Führungskräfte, Teams und Unternehmen in 1:1 Coachings, Workshops und Seminaren dafür, dass Sie souverän und selbstbewusst Ihre Zukunft sowie die Ihres Unternehmens gestalten.
          </p>
          <div class="hero-actions">
            <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
              <span>Unverbindlichen Kennenlerntermin vereinbaren</span>
              {SVG_ARROW}
            </a>
            <a href="#weitere-themenbereiche" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
              <span>Weitere Themenbereiche (Ausbau-Vorschau)</span>
            </a>
          </div>

          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val">25+ Jahre Erfahrung</span>
              <span class="hero-badge-lbl">Spitzensport-Mentaltraining &amp; Führungspraxis in Bankwesen, IT &amp; HR</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">4× Top 100 Trainer DACH</span>
              <span class="hero-badge-lbl">Ausgezeichnet durch Seminar.Inside in der Kategorie Performance</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">11 Zertifizierungen</span>
              <span class="hero-badge-lbl">9 Levels Wertesystem, Reiss Profile Master, CAS &amp; Business-Hypnose</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">Businesspark Sursee</span>
              <span class="hero-badge-lbl">Diskrete Coaching-Räume an der Allee 1b in Sursee sowie Inhouse &amp; Online</span>
            </div>
          </div>
        </div>

        <div class="hero-media-card">
          <img src="images/hero-wueest-paneduro.jpg" alt="Christine Wüest und Nino Paneduro – Innere Stärke entwickeln" data-slot="hero_image">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1rem;color:#181817;">Christine Wüest &amp; Nino Paneduro</div>
              <div style="font-size:0.8rem;color:var(--crimson);font-weight:700;">Mentoren, Coaches &amp; Ratgeber · Businesspark Sursee</div>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline-light btn-sm">
              <span>Smart-Anfrage testen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_core_pillars_section(is_v2=True)}

{render_founders_section(is_v2=True)}

  <!-- ORIGINAL-REFERENZLOGOS (KOMPLETT AUSGEARBEITET) -->
  <section id="referenzlogos" data-section="referenzlogos" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="ref_kicker">ORIGINAL-REFERENZLOGOS · BEREITS VOLLSTÄNDIG ÜBERNOMMEN</div>
        <h2 class="section-title" data-slot="ref_title">Alle 9 Referenz-Unternehmen und Partner-Organisationen im Überblick.</h2>
        <p class="section-desc" data-slot="ref_desc">
          Ihre bestehenden Referenz-Logos sind bereits in dieser Zeigeversion komplett eingebunden. Die ausführlichen Fallbeispiele und alle 10 Teilnehmerstimmen folgen im Ausbau-Modul unten.
        </p>
      </div>

      {render_reference_logos_grid()}
    </div>
  </section>

  <!-- KLARER TRENNER: WEITERE THEMENBEREICHE (FOLGEN BEIM GEMEINSAMEN AUSBAU) -->
  <section id="weitere-themenbereiche" data-section="weitere-themenbereiche" class="preview-scope-section">
    <div class="container">
      <div class="preview-scope-banner">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:14px;padding-bottom:14px;border-bottom:1px dashed rgba(249,178,49,0.45);">
          <span class="top-bar-badge">VORSCHAU-ENTWURF · AUSBAU-ÜBERSICHT FÜR WÜEST + PANEDURO</span>
        </div>
        <h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem);font-weight:800;color:#FFFFFF;margin-bottom:10px;">
          Weitere Themenbereiche (folgen beim gemeinsamen Ausbau)
        </h2>
        <p style="font-size:0.95rem;color:#E5E7EB;line-height:1.65;">
          In dieser <strong>Zeigeversion (Vorschau-Entwurf)</strong> sind <strong>2 Beispiel-Seiten</strong> (diese Startseite mit Hero, 4 Methoden-Säulen, Gründer-Porträts &amp; allen 9 Referenzlogos sowie die live funktionierende <strong>3-Schritte Smart-Anfrage</strong>) bereits für Sie ausgearbeitet. Die folgenden <strong>3 weiteren Themenbereiche</strong> sind als Vorschau-Module vorbereitet und werden beim gemeinsamen Ausbau schlüsselfertig ergänzt:
        </p>
      </div>

      <div class="grid-2">
        <!-- Vorschau-Karte 1: Angebots-Vertiefung & Seminar-Programme -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Themenbereich 1 · Folgt beim Ausbau</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:800;margin-bottom:8px;">Angebots-Vertiefung &amp; Seminar-Programme</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Detaillierte Darstellung Ihrer Coaching- und Trainingsformate inklusive Methodenkoffer, Abläufen und Nutzen für Führungskräfte und HR-Verantwortliche:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>1:1 Executive-Coaching, Standortbestimmung &amp; Prüfungs-/Wettkampf-Fokus</span></div>
              <div class="check-item">{SVG_CHECK}<span>Unternehmens-Workshops («TUNE IN» &amp; 9 Levels Wertesystem für Führungsteams)</span></div>
              <div class="check-item">{SVG_CHECK}<span>Reiss Motivation Profile (RMP), Aktiv-Wach-Hypnose &amp; Business-Hypnose</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Angebots-Vertiefung &amp; Seminar-Programme', '1:1 Executive-Coaching, 9 Levels Workshops, Reiss Profile &amp; Business-Hypnose', 'Christine Wüest &amp; Nino Paneduro')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <!-- Vorschau-Karte 2: Detaillierte Fallstudien & Teilnehmerstimmen -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Themenbereich 2 · Folgt beim Ausbau</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:800;margin-bottom:8px;">Detaillierte Fallstudien &amp; Teilnehmerstimmen</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Eigene Referenz-Seite mit sämtlichen 10 verifizierten Kundenstimmen im vollen Wortlaut sowie konkreten Praxis-Berichten aus Wirtschaft, Verwaltung und Spitzensport:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Führungs-Workshops beim Kanton Aargau (AWA &amp; Abteilung Recht) im «Herzberg» Uffikon &amp; Aarau</span></div>
              <div class="check-item">{SVG_CHECK}<span>Unternehmerinnen-Stimmen (Logo Parts GmbH, Soleil-Gesundheitspraxis, Zeitlos Sursee, BBackSoon)</span></div>
              <div class="check-item">{SVG_CHECK}<span>Über 10 Jahre Mentalcoaching im Spitzenhandball (QHL1 &amp; Sportmedizin)</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Detaillierte Fallstudien &amp; Teilnehmerstimmen', 'Alle 10 Original-Kundenstimmen &amp; Praxis-Fallbeispiele', 'Christine Wüest &amp; Nino Paneduro')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <!-- Vorschau-Karte 3: MentalFitnessCenter & Impulse -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Themenbereich 3 · Folgt beim Ausbau</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:800;margin-bottom:8px;">MentalFitnessCenter &amp; Impulse</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:12px;">
              Ihre bestehenden Begleit-Programme, das neue Buch sowie Ihre Bibliothek aus über 75 Führungs- und Mental-Impulsen übersichtlich gebündelt:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Inner Strength Circle</strong> (Jahresprogramm), <strong>45 Minuten über Mittag</strong> &amp; <strong>33 Daily Lunch Bites</strong></span></div>
              <div class="check-item">{SVG_CHECK}<span>Buch-Präsentation <strong>«Der Handball-Code»</strong> (12 echte Geschichten aus Nati &amp; Bundesliga) &amp; Keynotes</span></div>
              <div class="check-item">{SVG_CHECK}<span>Ausführliche Biografien, alle 11 Zertifizierungen &amp; Standort Businesspark Sursee</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('MentalFitnessCenter &amp; Impulse', 'Inner Strength Circle, 45 Min. über Mittag, 33 Daily Lunch Bites &amp; Buch «Der Handball-Code»', 'Christine Wüest &amp; Nino Paneduro')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>
"""


def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section data-section="kontakt-zentrale" style="padding: 56px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: DIREKTKONTAKT & BUSINESSPARK SURSEE -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; KENNENLERNTERMIN · SURSEE &amp; ONLINE</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:800;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Christine Wüest &amp; Nino Paneduro.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Schreiben Sie uns, rufen Sie uns an oder starten Sie rechts unseren geführten 3-Schritte Smart-Anfrage-Assistenten. Wir beantworten gerne Ihre Fragen zum Thema innere Stärke und stellen für Sie, Ihr Team oder Ihr Unternehmen ein passgenaues Konzept zusammen.
          </p>

          <img src="images/header-kontakt.jpg" alt="Christine Wüest und Nino Paneduro Kontakt Businesspark Sursee" style="width:100%;height:190px;object-fit:cover;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Standort &amp; Coaching-Räume Zentralschweiz</div>
              <div class="contact-direct-person">Nino Paneduro GmbH · Businesspark Sursee</div>
              <div class="contact-direct-links">Allee 1b · CH-6210 Sursee (Direkt an A2 / Bahnhof Sursee)</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Geschäftsführung · Resilienz &amp; Selbstführung</div>
              <div class="contact-direct-person">Christine Wüest (Dipl. Mental Coach &amp; Betriebswirtschafterin)</div>
              <div class="contact-direct-links">mail@innere-staerke.business · Tel. +41 78 606 20 56</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Vorsitzender der GL · Fokus, 9 Levels &amp; Hypnose</div>
              <div class="contact-direct-person">Nino Paneduro (4× Top 100 Trainer DACH · RMP Master)</div>
              <div class="contact-direct-links">mail@innere-staerke.business · Tel. +41 78 606 20 56 / +41 79 468 21 46</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Netzwerk &amp; Community</div>
              <div class="contact-direct-person">MentalFitnessCenter auf LinkedIn &amp; Facebook</div>
              <div class="contact-direct-links">linkedin.com/company/mentalfitnesscenter · UID: CHE-279.321.936 MWST</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · WÜEST + PANEDURO</div>
              <h2 style="font-size:1.35rem;font-weight:800;" id="wpWizardTitle">1. Worum geht es bei Ihrem Anliegen?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Begleitung: Christine Wüest &amp; Nino Paneduro</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Worum geht es?</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Rahmen &amp; Fokus</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill3">
              <span class="wp-step-num">3</span>
              <span>Kontakt &amp; Dossier</span>
            </div>
          </div>

          <form id="isContactForm" onsubmit="return wpSubmitIsLead(event)" novalidate>
            <div style="display:none;" aria-hidden="true">
              <label for="wpHoneypot">Website URL</label>
              <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off">
            </div>

            <!-- SCHRITT 1: WORUM GEHT ES? (4 AUSWAHLKARTEN) -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Führungskräfte- & Einzel-Coaching" onclick="wpSelectIsTopic('Führungskräfte- & Einzel-Coaching')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_COMPASS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Führungskräfte- &amp; Einzel-Coaching</span>
                  </div>
                  <span class="wp-role-desc">1:1 Sparring zu Selbstführung, Stressmanagement, 9 Levels, Reiss Profile oder Business-Hypnose</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Team-Training / Firmen-Workshop (Resilienz & Energie)" onclick="wpSelectIsTopic('Team-Training / Firmen-Workshop (Resilienz & Energie)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_USERS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Team-Training / Firmen-Workshop</span>
                  </div>
                  <span class="wp-role-desc">Massgeschneiderter Workshop (Resilienz &amp; Energie, 9 Levels Führungsteam oder TUNE IN)</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Impulsreferat / Keynote für Anlass" onclick="wpSelectIsTopic('Impulsreferat / Keynote für Anlass')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_AWARD}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Impulsreferat / Keynote für Anlass</span>
                  </div>
                  <span class="wp-role-desc">Inspirierender Vortrag für Führungstagung, Event oder Buch-Impuls «Der Handball-Code»</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Unverbindliches Erstgespräch im Businesspark Sursee / Online" onclick="wpSelectIsTopic('Unverbindliches Erstgespräch im Businesspark Sursee / Online')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_SPARKLES}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Unverbindliches Erstgespräch</span>
                  </div>
                  <span class="wp-role-desc">Persönliches Kennenlernen im Businesspark Sursee (Allee 1b) oder per Video-Call</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-gold" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Rahmen &amp; Fokus</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: RAHMEN & FOKUS -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Themenfokus / Schwerpunkt</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Selbstführung, Stressabbau, 9 Levels Werte, Fokus">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Teilnehmerkreis &amp; Ort</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. 1:1 in Sursee / Online oder Führungsteam (12 Pers.)">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Wunschzeitraum &amp; Durchführungsort</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnah (Kennenlerntermin in den nächsten 1–2 Wochen)" onclick="wpSelectIsUrgency('Zeitnah (Kennenlerntermin in den nächsten 1–2 Wochen)')">
                    <span class="wp-role-title">In den nächsten 1–2 Wochen</span>
                    <span class="wp-role-desc">Zeitnahes Erstgespräch in Sursee oder Online</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Planbar (Quartals- / Jahresplanung für Workshop oder Coaching)" onclick="wpSelectIsUrgency('Planbar (Quartals- / Jahresplanung für Workshop oder Coaching)')">
                    <span class="wp-role-title">Planbar (Kommende Wochen / Quartal)</span>
                    <span class="wp-role-desc">Konzept- &amp; Terminabstimmung für Coaching / Workshop</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Konkreter Event-Termin (Keynote / Kadersitzung)" onclick="wpSelectIsUrgency('Konkreter Event-Termin (Keynote / Kadersitzung)')">
                    <span class="wp-role-title">Konkreter Anlass / Kadersitzung</span>
                    <span class="wp-role-desc">Fixes Veranstaltungsdatum für Keynote / Retraite</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Dringend (Akute Herausforderung / Prüfungs- oder Veränderungsphase)" onclick="wpSelectIsUrgency('Dringend (Akute Herausforderung / Prüfungs- oder Veränderungsphase)')">
                    <span class="wp-role-title">Akute Situation / Kurzfristig</span>
                    <span class="wp-role-desc">Rasche Rückmeldung für zeitkritische Situation</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Persönliche Notiz / Ausgangslage (optional)</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Beschreiben Sie kurz Ihr Anliegen, Ihre Ziele oder Ihren Wunschtermin..."></textarea>
              </div>

              <div class="form-field" style="margin-bottom:18px;">
                <label class="form-label">Unterlagen, Programm-Skizze oder Situationsbild beifügen (optional, max. 3 Dateien)</label>
                <div class="wp-upload-zone">
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                    <span>Beilage / Bild auswählen (wird im 1-Seiten-PDF-Dossier eingebettet)</span>
                  </button>
                  <div style="font-size:0.75rem;color:var(--text-muted);margin-top:6px;" id="wpPhotoCounter">0 / 3 Beilagen ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier aufbereitet</div>
                  <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
                </div>
              </div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <span>Zurück zu Schritt 1</span>
                </button>
                <button type="button" class="btn-cta btn-cta-gold" style="width:100%;" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontaktdaten</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <!-- SCHRITT 3: KONTAKTDATEN & SOFORT-DOSSIER -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="wp-selftest-banner">
                <strong>Live-Vorschau &amp; Selbst-Test aktiv:</strong> Sie können diesen 3-Schritte-Assistenten jetzt live testen. Das System erzeugt sofort ein echtes <strong>1-Seiten-A4-PDF-Dossier</strong> im Erscheinungsbild von <strong>Wüest + Paneduro</strong> sowie die strukturierte WhatsApp- und E-Mail-Zusammenfassung.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Daniel Muster" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Firma / Organisation &amp; Funktion</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Muster AG Sursee · Mitglied der GL">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Ort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 6210 Sursee" oninput="wpCheckIsPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (optional)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Allee 1b">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                {SVG_CHECK}
                <span id="wpPlzBadgeText">PLZ 6210: Direkt beim Businesspark Sursee</span>
              </div>

              <div class="form-grid-2" style="margin-bottom:18px;">
                <div class="form-field">
                  <label for="contactEmail" class="form-label" data-slot="lbl_email">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" class="form-input" placeholder="name@unternehmen.ch" required>
                </div>
                <div class="form-field">
                  <label for="contactPhone" class="form-label" data-slot="lbl_phone">Telefon / Mobile (für Rückruf) *</label>
                  <input type="tel" id="contactPhone" name="phone" class="form-input" placeholder="+41 79 123 45 67" required>
                </div>
              </div>

              <div id="wpFormError" style="display:none;background-color:#FEE2E2;border:1px solid #FCA5A5;color:#991B1B;padding:10px 14px;border-radius:4px;font-size:0.84rem;margin-bottom:14px;"></div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <span>Zurück zu Schritt 2</span>
                </button>
                <button type="submit" class="btn-cta btn-cta-gold" id="wpSubmitBtn" style="width:100%;" data-slot="btn_submit">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>
          </form>

          <!-- SUCCESS COCKPIT -->
          <div class="wp-success-box" id="wpSuccessBox" aria-live="polite">
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
              <div style="display:flex;align-items:center;gap:10px;">
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--green);color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;">
                  {SVG_CHECK}
                </span>
                <div>
                  <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.08rem;color:var(--charcoal);">Anfrage &amp; 1-Seiten-PDF-Dossier erfolgreich erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:var(--charcoal);color:var(--gold);" id="wpResRef">#WP-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#FFFFFF;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständige Ansprechpartner (Businesspark Sursee):</div>
                <strong style="color:var(--charcoal);" id="wpResAssigned">Christine Wüest &amp; Nino Paneduro</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Verbindliches Rückmelde-Fenster:</div>
                <strong style="color:var(--gold-dark);" id="wpResCallback">Persönliche Rückmeldung</strong>
              </div>
            </div>

            <div>
              <div style="font-family:'Barlow',sans-serif;font-size:0.76rem;font-weight:800;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px;">
                Generierte WhatsApp- &amp; E-Mail-Zusammenfassung:
              </div>
              <div class="wp-wa-preview" id="wpResWaPreview">Anfrage-Zusammenfassung wird geladen...</div>
            </div>

            <div class="form-grid-2">
              <a href="kontakt.html" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-gold btn-sm" id="wpResPdfBtn" style="width:100%;">
                <span>1-Seiten-PDF-Dossier öffnen (A4)</span>
                {SVG_ARROW}
              </a>
              <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpResetWizard()">
                <span>Weitere Anfrage testen</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Führungskräfte- & Einzel-Coaching',
      urgency: 'Zeitnah (Kennenlerntermin in den nächsten 1–2 Wochen)',
      photos: []
    }};

    var wpIsRoleConfig = {{
      'Führungskräfte- & Einzel-Coaching': {{
        assignee: 'Christine Wüest & Nino Paneduro (1:1 Executive-Coaching)',
        l1: 'Themenfokus (Selbstführung, Stress, Werte, Fokus)',
        p1: 'z. B. Selbstführung, Stressmanagement, 9 Levels, Business-Hypnose',
        l2: 'Gewünschter Rahmen (Businesspark Sursee / Online)',
        p2: 'z. B. 1:1 im Businesspark Sursee oder Video-Call'
      }},
      'Team-Training / Firmen-Workshop (Resilienz & Energie)': {{
        assignee: 'Christine Wüest & Nino Paneduro (Team-Workshops & 9 Levels)',
        l1: 'Workshop-Fokus (z. B. Resilienz, 9 Levels, TUNE IN)',
        p1: 'z. B. 9 Levels Führungs-Workshop oder TUNE IN Mental-Stärke',
        l2: 'Teilnehmerkreis & Gruppengrösse',
        p2: 'z. B. Geschäftsleitung / Kader (10–15 Personen)'
      }},
      'Impulsreferat / Keynote für Anlass': {{
        assignee: 'Nino Paneduro & Christine Wüest (Keynotes & Der Handball-Code)',
        l1: 'Anlass & Thema des Impulsreferats',
        p1: 'z. B. Führungstagung, Kick-off oder «Der Handball-Code»',
        l2: 'Veranstaltungsort & ungefähre Teilnehmerzahl',
        p2: 'z. B. Luzern / Zürich · ca. 80 Teilnehmende'
      }},
      'Unverbindliches Erstgespräch im Businesspark Sursee / Online': {{
        assignee: 'Christine Wüest & Nino Paneduro (Businesspark Sursee)',
        l1: 'Worum geht es in erster Linie?',
        p1: 'z. B. Persönliches Kennenlernen & Standortbestimmung',
        l2: 'Bevorzugte Gesprächsform (Sursee Allee 1b / Online / Telefon)',
        p2: 'z. B. Vor Ort im Businesspark Sursee oder per MS Teams / Zoom'
      }}
    }};

    function wpUpdateIsHeader() {{
      var titles = {{
        1: '1. Worum geht es bei Ihrem Anliegen?',
        2: '2. Rahmen, Fokus & optionale Beilagen',
        3: '3. Kontaktdaten & Sofort-PDF-Dossier'
      }};
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl) tEl.textContent = titles[wpIsState.step] || titles[1];

      for (var i = 1; i <= 3; i++) {{
        var pane = document.getElementById('wpStep' + i);
        var pill = document.getElementById('wpStepPill' + i);
        if (pane) pane.classList.toggle('active', i === wpIsState.step);
        if (pill) {{
          pill.classList.remove('active', 'done');
          if (i === wpIsState.step) pill.classList.add('active');
          else if (i < wpIsState.step) pill.classList.add('done');
        }}
      }}
    }}

    function wpSelectIsTopic(topic) {{
      wpIsState.topic = topic;
      var tiles = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-topic') === topic);
      }}
      var cfg = wpIsRoleConfig[topic] || wpIsRoleConfig['Führungskräfte- & Einzel-Coaching'];
      var b = document.getElementById('wpActiveAssigneeBadge');
      if (b) b.textContent = cfg.assignee;
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (l1) l1.textContent = cfg.l1;
      if (i1) i1.placeholder = cfg.p1;
      if (l2) l2.textContent = cfg.l2;
      if (i2) i2.placeholder = cfg.p2;
    }}

    function wpSelectIsUrgency(urg) {{
      wpIsState.urgency = urg;
      var tiles = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-urg') === urg);
      }}
    }}

    function wpNextStep(target) {{
      wpIsState.step = target;
      wpUpdateIsHeader();
    }}

    function wpPrevStep() {{
      if (wpIsState.step > 1) {{
        wpIsState.step -= 1;
        wpUpdateIsHeader();
      }}
    }}

    function wpTriggerPhotoUpload() {{
      var inp = document.getElementById('wpPhotoInput');
      if (inp) inp.click();
    }}

    function wpCompressImageFile(file, cb) {{
      var reader = new FileReader();
      reader.onload = function(e) {{
        var img = new Image();
        img.onload = function() {{
          var maxSide = 1200;
          var w = img.width;
          var h = img.height;
          if (w > maxSide || h > maxSide) {{
            if (w >= h) {{ h = Math.round(h * (maxSide / w)); w = maxSide; }}
            else {{ w = Math.round(w * (maxSide / h)); h = maxSide; }}
          }}
          var canvas = document.createElement('canvas');
          canvas.width = w;
          canvas.height = h;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);
          cb(canvas.toDataURL('image/jpeg', 0.78));
        }};
        img.src = e.target.result;
      }};
      reader.readAsDataURL(file);
    }}

    function wpRenderPhotos() {{
      var box = document.getElementById('wpPhotoThumbs');
      var cnt = document.getElementById('wpPhotoCounter');
      if (cnt) cnt.textContent = wpIsState.photos.length + ' / 3 Beilagen ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier aufbereitet';
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpIsState.photos.length; i++) {{
        (function(idx) {{
          var wrap = document.createElement('div');
          wrap.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpIsState.photos[idx];
          im.alt = 'Beilage ' + (idx + 1);
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'wp-thumb-remove';
          btn.textContent = 'x';
          btn.onclick = function() {{ wpRemovePhoto(idx); }};
          wrap.appendChild(im);
          wrap.appendChild(btn);
          box.appendChild(wrap);
        }})(i);
      }}
    }}

    function wpHandlePhotoFiles(files) {{
      if (!files || !files.length) return;
      for (var i = 0; i < files.length; i++) {{
        if (wpIsState.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {{
          if (wpIsState.photos.length < 3) {{
            wpIsState.photos.push(b64);
            wpRenderPhotos();
          }}
        }});
      }}
    }}

    function wpRemovePhoto(idx) {{
      wpIsState.photos.splice(idx, 1);
      wpRenderPhotos();
    }}

    function wpCheckIsPlz(val) {{
      var badge = document.getElementById('wpPlzBadge');
      var txt = document.getElementById('wpPlzBadgeText');
      if (!badge || !txt) return;
      var m = String(val || '').match(/\\b(\\d{{4}})\\b/);
      if (!m) {{
        badge.className = 'wp-plz-badge';
        return;
      }}
      var plz = parseInt(m[1], 10);
      badge.className = 'wp-plz-badge in-area';
      if (plz >= 6000 && plz <= 6499) {{
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einzugsgebiet Zentralschweiz / Businesspark Sursee (Allee 1b)';
      }} else {{
        txt.textContent = 'PLZ ' + m[1] + ': Schweizweite Begleitung – Vor Ort, im Businesspark Sursee oder Online';
      }}
    }}

    function wpStripEmojisForDom(str) {{
      return String(str || '').replace(/[\\u{{1F300}}-\\u{{1FAFF}}\\u{{2600}}-\\u{{27BF}}]/gu, '').replace(/\\s+\\n/g, '\\n').trim();
    }}

    function wpResetWizard() {{
      wpIsState.step = 1;
      wpIsState.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('isContactForm');
      if (form) {{
        form.reset();
        form.style.display = 'block';
      }}
      var sBox = document.getElementById('wpSuccessBox');
      if (sBox) sBox.classList.remove('visible');
      var err = document.getElementById('wpFormError');
      if (err) err.style.display = 'none';
      var badge = document.getElementById('wpPlzBadge');
      if (badge) badge.className = 'wp-plz-badge';
      wpSelectIsTopic('Führungskräfte- & Einzel-Coaching');
      wpSelectIsUrgency('Zeitnah (Kennenlerntermin in den nächsten 1–2 Wochen)');
      wpUpdateIsHeader();
    }}

    function wpSubmitIsLead(e) {{
      if (e) e.preventDefault();
      var errBox = document.getElementById('wpFormError');
      if (errBox) errBox.style.display = 'none';

      var name = (document.getElementById('contactName').value || '').trim();
      var company = (document.getElementById('contactCompany').value || '').trim();
      var loc = (document.getElementById('contactLoc').value || '').trim();
      var street = (document.getElementById('contactStreet').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var msg = (document.getElementById('contactMessage').value || '').trim();
      var d1 = (document.getElementById('wpDetail1').value || '').trim();
      var d2 = (document.getElementById('wpDetail2').value || '').trim();
      var hp = (document.getElementById('wpHoneypot').value || '').trim();

      if (!name || (!phone && !email)) {{
        if (errBox) {{
          errBox.textContent = 'Bitte geben Sie Ihren Namen sowie Ihre E-Mail-Adresse oder Telefonnummer an.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var cfg = wpIsRoleConfig[wpIsState.topic] || wpIsRoleConfig['Führungskräfte- & Einzel-Coaching'];
      var extra = {{}};
      extra[cfg.l1] = d1 || 'Individuelle Abstimmung im Gespräch';
      extra[cfg.l2] = d2 || 'Businesspark Sursee / Online';

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';

      var payload = {{
        client_slug: '{client_slug}',
        source_page: '{source_page}',
        website_url: hp,
        category: wpIsState.topic,
        sparte: wpIsState.topic,
        urgency: wpIsState.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Anfrage zu ' + wpIsState.topic),
        extra_fields: extra,
        photos: wpIsState.photos,
        self_test_mode: true
      }};

      fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }})
      .then(function(r) {{ return r.json(); }})
      .then(function(res) {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (!res || !res.ok) {{
          if (errBox) {{
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuchen Sie es erneut.';
            errBox.style.display = 'block';
          }}
          return;
        }}
        document.getElementById('isContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Christine Wüest & Nino Paneduro';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Persönliche Rückmeldung';
        var chTxt = '1-Seiten-PDF-Dossier erstellt';
        if (res.email_sent) chTxt += ' · E-Mail mit PDF-Anhang zugestellt';
        if (res.whatsapp_sent) chTxt += ' · WhatsApp-Sofortmeldung zugestellt';
        document.getElementById('wpResChannels').textContent = chTxt;
        var pdfBtn = document.getElementById('wpResPdfBtn');
        if (pdfBtn && res.pdf_url) pdfBtn.href = res.pdf_url;
        var waBox = document.getElementById('wpResWaPreview');
        if (waBox) waBox.textContent = wpStripEmojisForDom(res.whatsapp_preview_text || '');
        document.getElementById('wpSuccessBox').classList.add('visible');
      }})
      .catch(function() {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (errBox) {{
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an mail@innere-staerke.business.';
          errBox.style.display = 'block';
        }}
      }});
      return false;
    }}

    (function() {{
      try {{
        var params = new URLSearchParams(window.location.search);
        var t = (params.get('thema') || '').toLowerCase();
        var map = {{
          'coaching': 'Führungskräfte- & Einzel-Coaching',
          'workshop': 'Team-Training / Firmen-Workshop (Resilienz & Energie)',
          'keynote': 'Impulsreferat / Keynote für Anlass',
          'erstgespraech': 'Unverbindliches Erstgespräch im Businesspark Sursee / Online'
        }};
        if (map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
      }} catch(err) {{}}
    }})();
  </script>
"""


# 3. Alle Seiten für Variante 1 (Komplettversion) schreiben
v1_pages = [
    ("index.html", "Innere Stärke entwickeln | Wüest + Paneduro – Mentoren, Coaches & Ratgeber Sursee", "startseite", V1_INDEX_BODY),
    ("angebot.html", "Angebot, Coaching, Workshops & 4 Säulen | Wüest + Paneduro Sursee", "angebot", V1_ANGEBOT_BODY),
    ("ueber-uns.html", "Über uns: Christine Wüest & Nino Paneduro | Mentoren, Coaches & Ratgeber", "ueber-uns", V1_UEBER_UNS_BODY),
    ("referenzen.html", "Referenzen & Alle 10 Kundenstimmen | Wüest + Paneduro Sursee", "referenzen", V1_REFERENZEN_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage | Wüest + Paneduro Businesspark Sursee", "kontakt", build_kontakt_body("innere-staerke", "preview-innere-staerke/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "Wüest + Paneduro (Zeigeversion / Vorschau-Entwurf) | Innere Stärke entwickeln", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | Wüest + Paneduro Sursee", "kontakt", build_kontakt_body("innere-staerke-v2", "preview-innere-staerke-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")


# 5. Partner-Attribution & Visitenkarten-Modal (#wpPartnerModal) injizieren
import subprocess
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

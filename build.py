"""Generates the static support / privacy site (FR + EN). Run: python3 build.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/ambinina1985/atlas-du-vivant-site"
CONTACT_ISSUES = REPO + "/issues/new"
# To show an e-mail address instead of (or in addition to) GitHub Issues, set it here:
CONTACT_EMAIL = ""

T = {
 "fr": {
  "lang": "fr", "name": "L’Atlas du Vivant", "other": "en", "otherLabel": "English",
  "nav": ("Assistance", "Confidentialité"),
  "home_title": "Explorez la planète. Découvrez sa faune.",
  "home_text": "Une application iPhone pour explorer les continents, découvrir chaque jour une nouvelle espèce et compléter votre atlas du vivant.",
  "home_eyebrow": "Application iPhone",
  "support_title": "Assistance",
  "support_intro": "Une question, un problème, une suggestion ? Les réponses aux questions fréquentes sont ci-dessous. Sinon, écrivez-nous : nous répondons généralement sous quelques jours.",
  "contact_title": "Nous contacter",
  "contact_issue": "Envoyer un message (GitHub)",
  "contact_email": "Écrire par e-mail",
  "contact_note": "Merci d’indiquer le modèle de votre iPhone, la version d’iOS et, si possible, une capture d’écran. N’indiquez jamais d’informations de paiement.",
  "faq_title": "Questions fréquentes",
  "faq": [
   ("Combien de découvertes gratuites ai-je ?", "La version gratuite permet 3 nouvelles découvertes par jour (la première découverte guidée ne compte pas). Le compteur repart à minuit, heure de votre iPhone. Les espèces déjà découvertes restent toujours accessibles."),
   ("Que débloque Premium ?", "Les découvertes illimitées, toutes les espèces du catalogue, toutes les collections, les quiz par pays, par continent et expert, ainsi que les comparaisons entre espèces. Premium existe en abonnement mensuel ou annuel, ou en achat unique à vie."),
   ("Comment restaurer mes achats ?", "Dans l’app : Profil › Premium › Restaurer les achats (le bouton est aussi présent en bas de l’écran Premium). Utilisez le même compte Apple que lors de l’achat."),
   ("Comment gérer ou annuler mon abonnement ?", "Dans l’app : Profil › Premium › Gérer l’abonnement. Ou sur l’iPhone : Réglages › [votre nom] › Abonnements. L’annulation doit intervenir au moins 24 heures avant la fin de la période en cours pour éviter le renouvellement."),
   ("Que deviennent mes espèces si l’abonnement s’arrête ?", "Elles restent dans votre collection. Seules les fonctions Premium (découvertes illimitées, contenus Premium non encore découverts…) ne sont plus disponibles."),
   ("Comment obtenir un remboursement ?", "Les paiements sont gérés par Apple. Faites votre demande sur reportaproblem.apple.com avec le compte Apple utilisé pour l’achat."),
   ("Où sont enregistrées mes données ?", "Uniquement sur votre iPhone : collection, favoris, quiz, badges et préférences. Il n’y a ni compte ni synchronisation en ligne : supprimer l’app efface ces données."),
   ("Comment changer la langue ?", "Profil › Langue : français, anglais ou langue du système. Le changement est immédiat."),
   ("L’app fonctionne-t-elle hors ligne ?", "Oui pour la collection, les fiches, les photos et les quiz. La carte nécessite une connexion ; hors ligne, l’onglet Explorer propose une vue en liste."),
   ("D’où viennent les photos et les informations ?", "Les photographies proviennent de Wikimedia Commons, sous licences libres, avec l’auteur crédité sur chaque fiche (Profil › Sources et crédits). Les statuts de conservation font référence à la Liste rouge de l’UICN. Vous avez repéré une erreur ? Écrivez-nous."),
  ],
  "privacy_title": "Politique de confidentialité",
  "privacy_updated": "Dernière mise à jour : 11 octobre 2026",
  "privacy": [
   ("Aucun compte requis", "L’Atlas du Vivant fonctionne sans inscription. Nous ne demandons ni nom, ni adresse e-mail, ni numéro de téléphone."),
   ("Données conservées sur l’appareil", "Votre collection, vos favoris, vos résultats de quiz, vos badges et vos préférences sont enregistrés localement sur votre iPhone. Ils ne sont pas envoyés sur nos serveurs. Supprimer l’application efface ces données."),
   ("Pas de suivi ni de publicité", "L’application ne contient ni publicité, ni outil de suivi publicitaire, ni kit d’analyse tiers. Nous ne vendons et ne partageons aucune donnée."),
   ("Localisation", "L’application n’accède pas à votre position. La carte affiche le monde sans vous localiser."),
   ("Achats", "Les achats et abonnements sont traités par Apple. Nous ne recevons jamais vos informations de paiement. L’application vérifie uniquement auprès de l’App Store quels contenus vous sont accessibles."),
   ("Cartes et notifications", "La carte utilise Apple Maps, soumis à la politique de confidentialité d’Apple. Les rappels quotidiens sont des notifications locales programmées sur votre appareil, uniquement si vous les activez."),
   ("Enfants", "L’application ne collecte aucune donnée personnelle, y compris auprès des enfants."),
   ("Contact", "Pour toute question relative à la confidentialité, utilisez la page Assistance."),
  ],
  "footer_photo": "Photo : renard polaire par Jonatan Pie (CC0), via Wikimedia Commons.",
 },
 "en": {
  "lang": "en", "name": "The Living Atlas", "other": "fr", "otherLabel": "Français",
  "nav": ("Support", "Privacy"),
  "home_title": "Explore the planet. Discover its wildlife.",
  "home_text": "An iPhone app to explore the continents, discover a new species every day and complete your living atlas.",
  "home_eyebrow": "iPhone app",
  "support_title": "Support",
  "support_intro": "A question, a problem, a suggestion? Answers to common questions are below. Otherwise, get in touch: we usually reply within a few days.",
  "contact_title": "Contact us",
  "contact_issue": "Send a message (GitHub)",
  "contact_email": "Send an e-mail",
  "contact_note": "Please include your iPhone model, iOS version and, if possible, a screenshot. Never include payment details.",
  "faq_title": "Frequently asked questions",
  "faq": [
   ("How many free discoveries do I get?", "The free version includes 3 new discoveries a day (the first guided discovery doesn’t count). The counter resets at midnight, iPhone time. Species you have already discovered always remain available."),
   ("What does Premium unlock?", "Unlimited discoveries, every species in the catalogue, every collection, country, continent and expert quizzes, and species comparisons. Premium is available as a monthly or yearly subscription, or as a one-time lifetime purchase."),
   ("How do I restore my purchases?", "In the app: Profile › Premium › Restore purchases (the button is also at the bottom of the Premium screen). Use the same Apple Account you purchased with."),
   ("How do I manage or cancel my subscription?", "In the app: Profile › Premium › Manage subscription. Or on your iPhone: Settings › [your name] › Subscriptions. Cancel at least 24 hours before the end of the current period to avoid renewal."),
   ("What happens to my species if my subscription ends?", "They stay in your collection. Only Premium features (unlimited discoveries, undiscovered Premium content…) become unavailable."),
   ("How do I get a refund?", "Payments are handled by Apple. Request a refund at reportaproblem.apple.com with the Apple Account used for the purchase."),
   ("Where is my data stored?", "Only on your iPhone: collection, favourites, quizzes, badges and preferences. There is no account and no online sync: deleting the app erases this data."),
   ("How do I change the language?", "Profile › Language: English, French or system language. The change is instant."),
   ("Does the app work offline?", "Yes for your collection, field guides, photos and quizzes. The map needs a connection; offline, the Explore tab shows a list view."),
   ("Where do the photos and facts come from?", "Photographs come from Wikimedia Commons under free licences, with the author credited on each field guide (Profile › Sources and credits). Conservation statuses refer to the IUCN Red List. Spotted a mistake? Let us know."),
  ],
  "privacy_title": "Privacy Policy",
  "privacy_updated": "Last updated: October 11, 2026",
  "privacy": [
   ("No account required", "The Living Atlas works without signing up. We never ask for your name, email address or phone number."),
   ("Data kept on your device", "Your collection, favourites, quiz results, badges and preferences are stored locally on your iPhone. They are not sent to our servers. Deleting the app erases this data."),
   ("No tracking, no ads", "The app contains no ads, no advertising trackers and no third-party analytics kits. We do not sell or share any data."),
   ("Location", "The app does not access your location. The map shows the world without locating you."),
   ("Purchases", "Purchases and subscriptions are handled by Apple. We never receive your payment details. The app only checks with the App Store which content you can access."),
   ("Maps and notifications", "The map uses Apple Maps, subject to Apple’s privacy policy. Daily reminders are local notifications scheduled on your device, only if you turn them on."),
   ("Children", "The app collects no personal data, including from children."),
   ("Contact", "For any privacy question, please use the Support page."),
  ],
  "footer_photo": "Photo: arctic fox by Jonatan Pie (CC0), via Wikimedia Commons.",
 },
}

def page(lang, slug, title, body, hero=False):
    t = T[lang]
    suffix = "" if lang == "fr" else "-en"
    other_suffix = "-en" if lang == "fr" else ""
    home = "index.html" if lang == "fr" else "index-en.html"
    other_page = {"index": "index", "support": "support", "privacy": "privacy"}[slug] + other_suffix + ".html"
    hero_html = ""
    if hero:
        hero_html = f'''<section class="hero"><div class="wrap">
<div class="eyebrow">{t["home_eyebrow"]}</div>
<h1>{t["home_title"]}</h1>
<p>{t["home_text"]}</p>
</div></section>'''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {t["name"]}</title>
<meta name="description" content="{t["home_text"]}">
<link rel="icon" href="assets/icon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
<img src="assets/icon.png" alt="">
<a class="name" href="{home}">{t["name"]}</a>
<nav><a href="support{suffix}.html">{t["nav"][0]}</a><a href="privacy{suffix}.html">{t["nav"][1]}</a><a class="lang" href="{other_page}" hreflang="{t["other"]}">{t["otherLabel"]}</a></nav>
</div></header>
{hero_html}
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
<a href="support{suffix}.html">{t["nav"][0]}</a><a href="privacy{suffix}.html">{t["nav"][1]}</a>
<p>{t["footer_photo"]}</p>
</div></footer>
</body>
</html>
'''

def contact(t):
    links = f'<a class="button" href="{CONTACT_ISSUES}">{t["contact_issue"]}</a>'
    if CONTACT_EMAIL:
        links = f'<a class="button" href="mailto:{CONTACT_EMAIL}">{t["contact_email"]}</a> &nbsp; ' + links
    return f'<div class="card"><h2 style="margin-top:0">{t["contact_title"]}</h2><p>{links}</p><p class="muted">{t["contact_note"]}</p></div>'

for lang, t in T.items():
    suffix = "" if lang == "fr" else "-en"
    home_body = f'''<div class="card"><h2 style="margin-top:0">{t["nav"][0]}</h2><p>{t["support_intro"]}</p><p><a class="button" href="support{suffix}.html">{t["nav"][0]}</a></p></div>
<div class="card"><h2 style="margin-top:0">{t["nav"][1]}</h2><p><a href="privacy{suffix}.html">{t["privacy_title"]}</a></p></div>'''
    open(os.path.join(HERE, f"index{suffix}.html"), "w").write(page(lang, "index", t["name"], home_body, hero=True))
    faq = "".join(f'<h3>{q}</h3><p>{a}</p>' for q, a in t["faq"])
    support_body = f'<h1>{t["support_title"]}</h1><p>{t["support_intro"]}</p>{contact(t)}<h2>{t["faq_title"]}</h2>{faq}'
    open(os.path.join(HERE, f"support{suffix}.html"), "w").write(page(lang, "support", t["support_title"], support_body))
    sections = "".join(f'<h2>{h}</h2><p>{p}</p>' for h, p in t["privacy"])
    privacy_body = f'<h1>{t["privacy_title"]}</h1><p class="muted">{t["privacy_updated"]}</p>{sections}'
    open(os.path.join(HERE, f"privacy{suffix}.html"), "w").write(page(lang, "privacy", t["privacy_title"], privacy_body))
print("built")

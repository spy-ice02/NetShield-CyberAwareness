import os

pages = [
    {
        "filename": "social-media-theft.html",
        "title": "Social Media Identity Theft",
        "theme": "accent",
        "gradient_css": "", 
        "gradient_class": "gradient-text",
        "icon": "fa-user-secret",
        "intro_title": "The Digital Doppelgänger",
        "intro_desc": "Fraudsters target your digital persona. By stealing information you casually share online, they can perfectly impersonate you or completely commandeer your social accounts to scam your entire network.",
        "golden_rule": "Protect your digital footprint. <u class='decoration-accent decoration-wavy underline-offset-4'>Always verify urgent money requests via a direct voice call!</u>",
        "modus": [
            ("Profile Cloning", "fa-user-ninja", "Scammers copy your photos and create an identical fake profile. They then message your friends lists asking for small amounts of money due to a fabricated emergency."),
            ("OTP Interception", "fa-mobile-screen", "You receive a message from a 'friend' saying they accidentally sent their login OTP to your number. Once you share it, your WhatsApp is immediately hacked."),
            ("Romance Scams", "fa-heart-crack", "Scammers spend months building trust and emotional connection through dating apps before concocting an elaborate story requiring immediate financial help."),
            ("Fake Investment Gurus", "fa-chart-line", "Hackers take over a legitimate friend's account and post screenshots of massive crypto profits, tricking you into 'investing' on a fake portal.")
        ],
        "prevention": [
            ("Lock Your Profile", "Ensure your photos, posts, and friend list are restricted strictly to 'Friends Only'. Never keep your friend list public."),
            ("Enable 2-Step Verification", "Activate 2FA with an authenticator app (like Google Authenticator) on all email and social media accounts."),
            ("Never Share OTPs", "Never forward a 6-digit SMS code to anyone, even if they claim to be a close friend or family member."),
            ("Verify Emergency Requests", "If a contact asks for financial help abruptly via text, literally call them on the phone and speak to them directly.")
        ],
        "cases": [
            ("Delhi", "Recent", "WhatsApp Extortion", "Victim lost access to WhatsApp. Scammers messaged all 500 contacts, successfully getting 10 people to transfer a total of ₹1L."),
            ("Mumbai", "Recent", "Facebook Clone Scam", "Senior citizen transferred ₹50,000 to an account thinking his nephew was critically injured, based on a DM from a cloned profile."),
            ("Kolkata", "Recent", "Instagram Verification Fraud", "A small business owner paid ₹20,000 to a fake 'Meta Support' offering a blue verified badge, which led to a complete account takeover."),
            ("Chennai", "Recent", "Crypto Guru Impersonation", "A hacked account of a trusted friend posted fake Bitcoin gains. The victim deposited ₹5L into the fraudster's untraceable wallet."),
            ("Hyderabad", "Recent", "Romance Extortion Trap", "A victim sent ₹3L for 'customs clearance' for supposedly expensive gifts sent by an online friend they met on a dating app."),
            ("Pune", "Recent", "Fake Medical Fundraiser", "A scammer created a replica profile of a known local activist and successfully collected ₹80,000 in fake medical donations from genuine well-wishers.")
        ]
    },
    {
        "filename": "task-scams.html",
        "title": "Task & Part-Time Job Scams",
        "theme": "emerald-500",
        "gradient_css": ".emerald-500-gradient-text { background: linear-gradient(to right, #10b981, #34d399); -webkit-background-clip: text; background-clip: text; color: transparent; }",
        "gradient_class": "emerald-500-gradient-text",
        "icon": "fa-briefcase",
        "intro_title": "The Illusion of Easy Money",
        "intro_desc": "Work-from-home task scams prey on the desire for extra income. They start by offering real, micro-payments for effortless tasks to build trust, before trapping victims in a psychological 'sunk-cost' vortex.",
        "golden_rule": "Legitimate jobs pay you. <u class='decoration-emerald-500 decoration-wavy underline-offset-4'> NEVER pay a 'deposit' to unlock a job or a higher commission tier!</u>",
        "modus": [
            ("The Bait (Small Payouts)", "fa-fish", "You are contacted via WhatsApp/Telegram offering ₹50 for liking YouTube videos or leaving 5-star hotel reviews. They actually pay you the first few times."),
            ("The Premium/Prepaid Task", "fa-gem", "Once trust is established, you're assigned a 'prepaid task' where you must deposit ₹2000 to earn a 30% commission. It works the first time."),
            ("The Sunk-Cost Trap", "fa-link", "The tasks require larger and larger deposits (₹50k, ₹1L). When you try to withdraw, they claim your 'merchant score' is low and you must do one final task to unlock funds."),
            ("The Account Freeze", "fa-snowflake", "After draining all your savings, the scammers freeze your dashboard account and delete the Telegram group. Your money is gone forever.")
        ],
        "prevention": [
            ("Verify the Recruiter", "Real companies do not hire via anonymous Telegram/WhatsApp messages offering ₹5,000/day for 'liking videos'."),
            ("Recognize the Bait", "If a job involves 'recharging' an account with cryptocurrency or UPI to complete virtual orders, it is a guaranteed scam."),
            ("Do Not Chase Losses", "If your money gets 'stuck' demanding a higher deposit to withdraw, STOP. Any further transfer will also be stolen."),
            ("Beware of Group Chat Illusions", "Those 50 people in the Telegram group posting screenshots of their 'profits' are all bots or the scammers themselves.")
        ],
        "cases": [
            ("Bangalore", "Recent", "Software Engineer Ruined", "Techie lost ₹25 Lakhs trying to withdraw his initial ₹5 Lakh 'investment' in a fake hotel review app. Borrowed heavily to unlock his frozen dashboard."),
            ("Pune", "Recent", "YouTube Like Scam", "College student lost ₹1.2L of tuition fees. Scammers paid him ₹150 three times perfectly before initiating the massive prepaid deposit trap."),
            ("Ahmedabad", "Recent", "Movie Review Fraud", "A housewife lost ₹8 Lakhs evaluating 'IMDb ratings' on a counterfeit website, lured by the promise of earning ₹10,000 daily."),
            ("Jaipur", "Recent", "Crypto Rating Trap", "Retiree drained his entire ₹15 Lakh pension into a 'Telegram Trading Group' where bots constantly praised an admins fake crypto signals."),
            ("Lucknow", "Recent", "Product Rating Scam", "A teacher deposited ₹3 Lakhs to increase her 'merchant score' on a fake international e-commerce website so she could withdraw her imaginary earnings."),
            ("Surat", "Recent", "Freelance Graphic Trap", "A designer was hired for freelance work, but was told he must first purchase a ₹40,000 'ID Card and Software License' via UPI to get his first paycheck.")
        ]
    },
    {
        "filename": "digital-arrest.html",
        "title": "Digital Arrest Extortion",
        "theme": "purple-500",
        "gradient_css": ".purple-500-gradient-text { background: linear-gradient(to right, #a855f7, #c084fc); -webkit-background-clip: text; background-clip: text; color: transparent; }",
        "gradient_class": "purple-500-gradient-text",
        "icon": "fa-video",
        "intro_title": "The Virtual Interrogation",
        "intro_desc": "Digital Arrest is a highly coordinated psychological terror attack. Scammers successfully impersonate Law Enforcement (CBI, Customs, Narcotics) over video calls to paralyze victims with fear of immediate imprisonment.",
        "golden_rule": "Indian authorities do not use Skype. <u class='decoration-purple-500 decoration-wavy underline-offset-4'>No real agency will EVER ask you to transfer funds to 'verify' them.</u>",
        "modus": [
            ("The Courier Threat", "fa-box-open", "You receive a robotic call claiming a FedEx parcel containing illegal passports/MDMA linked to your Aadhaar was intercepted at customs."),
            ("The Transfer to 'Police'", "fa-phone", "You are 'transferred' to a fake Cyber Crime division line. A man in a real-looking police uniform demands you switch to a Skype video call."),
            ("The Digital Arrest", "fa-lock", "You are told you are 'digitally arrested', must stay on camera 24/7, and cannot tell anyone. Fake Supreme Court warrants are shown to you."),
            ("The Verification Transfer", "fa-money-bill-transfer", "They claim you must transfer all your savings to an 'RBI safe account' for auditing to prove your innocence. They promise to return it in 2 hours.")
        ],
        "prevention": [
            ("Disconnect Immediately", "No law enforcement agency in India conducts arrests or interrogations via Skype or WhatsApp video calls. Hang up immediately."),
            ("Verify the Claim", "If told a courier had illegal goods, do not panic. Ask for an airway bill and check directly on the official courier website."),
            ("Never Transfer Security Deposits", "Police, CBI, and Customs NEVER ask citizens to transfer money to a 'safe account' to dismiss an investigation."),
            ("Call 1930 Helpline", "If you are trapped in a call and feeling threatened, immediately use another phone to call the national cybercrime helpline 1930.")
        ],
        "cases": [
            ("Noida", "Recent", "Doctor Duped", "Senior doctor transferred ₹1.5 Cr to 'RBI safe accounts' after being held under 'digital arrest' on Skype for 48 straight hours by fake CBI officers."),
            ("Hyderabad", "Recent", "FedEx Trap", "Software developer lost ₹45 Lakhs after scammers faked an arrest warrant claiming drugs were found in a parcel bound for Taiwan under his name."),
            ("Bhopal", "Recent", "Fake TRAI Alert", "An executive received a robot call claiming all his mobile numbers would be blocked for illegal activities. He paid ₹12 Lakhs to a 'Cyber Inspector'."),
            ("Chandigarh", "Recent", "Telecom Extortion", "A college professor was terrified into liquidating ₹60 Lakhs in mutual funds after being convinced by a fake warrant bearing the official state emblem."),
            ("Indore", "Recent", "Fake Custom Official", "A woman lost ₹8 Lakhs over 5 hours on WhatsApp video call to a man in a police uniform who claimed she was linked to an international money laundering syndicate."),
            ("Kochi", "Recent", "Passport Fraud", "A businessman was led to believe his passport had been used for human trafficking. To 'verify his bank statements', he unknowingly granted AnyDesk access, losing ₹22 Lakhs.")
        ]
    },
    {
        "filename": "loan-apps.html",
        "title": "Predatory Loan Apps",
        "theme": "orange-500",
        "gradient_css": ".orange-500-gradient-text { background: linear-gradient(to right, #f97316, #fb923c); -webkit-background-clip: text; background-clip: text; color: transparent; }",
        "gradient_class": "orange-500-gradient-text",
        "icon": "fa-mobile-screen-button",
        "intro_title": "The Debt Trap",
        "intro_desc": "Predatory Chinese-linked instant loan apps bypass banking norms to offer rapid, tiny loans. Hidden in the terms is the permission to completely harvest your contact list and photo gallery for ruthless blackmail.",
        "golden_rule": "If an app demands contact access, uninstall it. <u class='decoration-orange-500 decoration-wavy underline-offset-4'>Never borrow from unverified, non-RBI registered applications.</u>",
        "modus": [
            ("The Data Harvest", "fa-database", "You download a 'Cash Fast' app. It demands blanket permissions to your Contacts, Gallery, and SMS to 'assess creditworthiness'. It immediately steals this data."),
            ("The 7-Day Extortion", "fa-calendar-day", "You borrow ₹5000. They deposit only ₹3000 but demand ₹7000 repayment within exactly 7 days, applying illegal, astronomical interest rates."),
            ("The Morphing Threat", "fa-image", "If you delay by a day, they use photos stolen from your gallery, morph them into pornographic material, and threaten to send them to your family."),
            ("The Social Shaming", "fa-users", "They create WhatsApp groups adding all your stolen contacts (boss, parents, friends), branding you a 'thief' and sharing the morphed photos to force payment.")
        ],
        "prevention": [
            ("Check RBI Registration", "Only use financial apps explicitly linked to RBI-registered Non-Banking Financial Companies (NBFCs). Check their official status online."),
            ("Deny Contact Permissions", "A legitimate lending app has absolutely no reason to require access to your entire phonebook or photo gallery."),
            ("Ignore Shaming Tactics", "If blackmailed, do not pay. Paying them only validates you as a target, and they will demand more money endlessly."),
            ("Report to Law Enforcement", "Immediately file an FIR and report the app to Google Play Store and the Cyber Crime portal.")
        ],
        "cases": [
            ("Chennai", "Recent", "Tragic Tragedy", "A young professional took his life after loan recovery agents morphed his photos and sent them to his entire office for defaulting on a ₹3000 app loan."),
            ("Gurugram", "Recent", "Call Center Busted", "Police raided an illegal setup where 100 telecallers were specifically assigned to abuse and extort Indian borrowers using morphed imagery on behalf of foreign handlers."),
            ("Patna", "Recent", "Multiple App Trap", "To briefly pay off a ₹5000 loan from App A, a victim borrowed from App B, triggering a cascade where they owed ₹4 Lakhs across 32 illegal apps within a month."),
            ("Bhubaneswar", "Recent", "Contact Defamation", "Recovery agents created a WhatsApp group titled 'Chor' (Thief), added the victim's boss and mother, and posted abusive messages non-stop for a delayed ₹2000 payment."),
            ("Nagpur", "Recent", "Fake NOC Scam", "Even after a victim paid the exorbitant ₹15,000 back, the app handlers claimed the 'No Objection Certificate' fee was unpaid, continuing to harass their contacts."),
            ("Dehradun", "Recent", "Data Privacy Breach", "A student who merely installed an app to check eligibility without accepting any loan had his entire gallery exported to overseas servers for future blackmail.")
        ]
    }
]

import re
with open("phishing-smishing.html", "r", encoding="utf-8") as f:
    template = f.read()

for p in pages:
    content = template
    # Replace basic theme colors
    content = content.replace("danger", p["theme"])
    content = content.replace("danger-gradient-text", p["gradient_class"])
    
    # Add new css rules if any
    if p["gradient_css"]:
        content = content.replace("</style>", f"    {p['gradient_css']}\n    </style>")
        
    # Replace text content
    content = re.sub(r"<title>.*?</title>", f"<title>NetShield - {p['title']}</title>", content)
    content = re.sub(r"<h1 class=\"text-4xl md:text-5xl font-extrabold mb-4 text-white\">.*?</h1>", f"<h1 class=\"text-4xl md:text-5xl font-extrabold mb-4 text-white\">{p['title']}</h1>", content)
    content = re.sub(r"<p class=\"text-lg text-gray-400\">.*?</p>", f"<p class=\"text-lg text-gray-400\">{p['intro_desc']}</p>", content, count=1)
    
    # Intro
    content = re.sub(r"<i class=\"fa-solid fa-[^\"]* absolute -right-4 -bottom-4 text-9xl", f"<i class=\"fa-solid {p['icon']} absolute -right-4 -bottom-4 text-9xl", content)
    content = re.sub(r"<h2 class=\"text-2xl font-bold mb-4 text-white flex items-center\"><i class=\"fa-solid fa-[^\"]* text", f"<h2 class=\"text-2xl font-bold mb-4 text-white flex items-center\"><i class=\"fa-solid {p['icon']} text", content)
    content = re.sub(r"<h2 class=\"text-2xl font-bold mb-4 text-white flex items-center\">.*?</h2>", f"<h2 class=\"text-2xl font-bold mb-4 text-white flex items-center\"><i class=\"fa-solid {p['icon']} text-{p['theme']} mr-3\"></i> {p['intro_title']}</h2>", content)
    
    content = re.sub(r"<p class=\"text-gray-300 mb-6 leading-relaxed\">.*?</p>", f"<p class=\"text-gray-300 mb-6 leading-relaxed\">\n                        {p['intro_desc']}\n                    </p>", content)
    content = re.sub(r"<p class=\"text-white text-lg font-medium\">.*?</p>", f"<p class=\"text-white text-lg font-medium\">{p['golden_rule']}</p>", content)
    
    # Modus
    # We find the grid containing 4 cards
    modus_html = ""
    for idx, (m_title, m_icon, m_desc) in enumerate(p["modus"]):
        modus_html += f'''                    <!-- Card {idx+1} -->
                    <div class="glass-panel p-6 rounded-xl border border-slate-700 hover:border-{p['theme']}/50 transition">
                        <h3 class="text-xl font-bold text-{p['theme']} mb-3 flex items-center"><i class="fa-solid {m_icon} mr-2"></i> {m_title}</h3>
                        <p class="text-sm text-gray-400 flex-1">{m_desc}</p>
                    </div>\n'''
    
    # replace the inner of the grid
    content = re.sub(r'(<div class="grid md:grid-cols-2 gap-6">)(.*?)(</section>)', lambda m: m.group(1) + "\n" + modus_html + "                </div>\n            " + m.group(3), content, flags=re.DOTALL, count=1)
    
    # Prevention
    prev_html = ""
    for idx, (pr_title, pr_desc) in enumerate(p["prevention"]):
        prev_html += f'''                        <li class="flex items-start">
                            <div class="shrink-0 w-10 h-10 rounded-full bg-{p['theme']}/20 flex items-center justify-center text-{p['theme']} mr-4 mt-1 border border-{p['theme']}/50"><i class="fa-solid fa-{idx+1} font-bold"></i></div>
                            <div>
                                <h4 class="text-lg font-bold text-white mb-1">{pr_title}</h4>
                                <p class="text-gray-400 text-sm">{pr_desc}</p>
                            </div>
                        </li>\n'''
    content = re.sub(r'(<ul class="space-y-6">)(.*?)(</ul>)', lambda m: m.group(1) + "\n" + prev_html + "                    " + m.group(3), content, flags=re.DOTALL)
    
    # Cases
    cases_html = ""
    for idx, case in enumerate(p["cases"]):
        cases_html += f'''                            <!-- {idx+1} -->
                            <div class="bg-slate-800 p-4 rounded-lg border-l-4 border-{p['theme']}">
                                <div class="flex justify-between text-xs text-gray-500 mb-2"><span><i class="fa-solid fa-location-dot mr-1"></i> {case[0]}</span> <span>{case[1]}</span></div>
                                <h4 class="font-bold text-white mb-1">{case[2]}</h4>
                                <p class="text-sm text-gray-400">{case[3]}</p>
                            </div>\n'''
    
    # Add a duplicate of the first element to allow seamless infinite scrolling CSS loop
    case = p["cases"][0]
    cases_html += f'''                            <!-- Duplicate the list for seamless infinite looping -->
                            <!-- 1 (Duplicate) -->
                            <div class="bg-slate-800 p-4 rounded-lg border-l-4 border-{p['theme']} mt-4">
                                <div class="flex justify-between text-xs text-gray-500 mb-2"><span><i class="fa-solid fa-location-dot mr-1"></i> {case[0]}</span> <span>{case[1]}</span></div>
                                <h4 class="font-bold text-white mb-1">{case[2]}</h4>
                                <p class="text-sm text-gray-400">{case[3]}</p>
                            </div>\n'''
    
    # replacing scrolling content
    content = re.sub(r'(<div class="scrolling-content space-y-4">)(.*?)(</div>\s*</div>\s*</div>\s*</section>)', lambda m: m.group(1) + "\n" + cases_html + "                        " + m.group(3), content, flags=re.DOTALL)
    
    with open(p["filename"], "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {p['filename']} with 6 unique case reports.")

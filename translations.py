"""
LivrCheck bilingual content (English + Hindi).

NOTE ON HINDI TEXT:
The Hindi strings below are a first-pass draft translation written to be
clear and medically neutral. Per the LivrCheck project plan, they should be
reviewed by a native Hindi speaker (ideally with some health/medical
familiarity) before this tool is shared publicly. Look for the
"NEEDS_NATIVE_REVIEW" flag in this file's docstring as a reminder — nothing
here has been reviewed by a native speaker yet.
"""

TEXT = {
    "en": {
        "app_title": "LivrCheck",
        "app_subtitle": "Know your liver fibrosis risk from a routine blood test",
        "language_label": "Language / भाषा",
        "intro_heading": "What is this tool?",
        "intro_body": (
            "LivrCheck calculates your **FIB-4 score**, a clinically validated "
            "estimate of liver fibrosis (scarring) risk, using four numbers "
            "from a standard blood test: your age, AST, ALT, and platelet "
            "count. These are part of a routine Liver Function Test (LFT) "
            "and Complete Blood Count (CBC) — the kind of report many "
            "families already have sitting in a drawer."
        ),
        "not_alcohol_heading": "This is not about alcohol",
        "not_alcohol_body": (
            "Non-Alcoholic Fatty Liver Disease (NAFLD) is caused by diet, "
            "obesity, diabetes, and sedentary lifestyle — not alcohol. "
            "Many Indian families assume a fatty liver diagnosis means an "
            "alcohol problem, which can delay proper diagnosis and care by "
            "years."
        ),
        "form_heading": "Enter your blood test values",
        "age_label": "Age (years)",
        "ast_label": "AST (U/L)",
        "ast_help": "Sometimes labeled SGOT on your report",
        "alt_label": "ALT (U/L)",
        "alt_help": "Sometimes labeled SGPT on your report",
        "platelets_label": "Platelet count (×10⁹/L, i.e. lakhs/cmm × 100)",
        "platelets_help": (
            "If your report shows platelets in lakhs/cmm (e.g. 2.5 lakh/cmm), "
            "multiply by 100 to get ×10⁹/L (e.g. 2.5 → 250)."
        ),
        "context_heading": "A few more questions (optional, but useful context)",
        "bmi_heading": "Body Mass Index (BMI)",
        "height_label": "Height (cm)",
        "weight_label": "Weight (kg)",
        "diabetes_label": "Do you have diabetes or pre-diabetes?",
        "family_history_label": (
            "Does anyone in your immediate family have fatty liver disease, "
            "cirrhosis, or metabolic syndrome (diabetes + obesity + high BP)?"
        ),
        "yes": "Yes",
        "no": "No",
        "not_sure": "Not sure",
        "calculate_button": "Calculate my FIB-4 score",
        "results_heading": "Your Results",
        "score_label": "FIB-4 Score",
        "tier_low": "Low Risk",
        "tier_intermediate": "Intermediate Risk",
        "tier_high": "High Risk",
        "tier_low_explanation": (
            "Your score suggests a low likelihood of advanced liver "
            "fibrosis. In studies, a score in this range correctly rules out "
            "advanced fibrosis about 91% of the time (negative predictive "
            "value ~90.7%)."
        ),
        "tier_intermediate_explanation": (
            "Your score is in an intermediate zone. This does not confirm "
            "fibrosis, but it means it cannot be ruled out either. Further "
            "evaluation is recommended."
        ),
        "tier_high_explanation": (
            "Your score is above the high-risk threshold. Scores above 3.25 "
            "are associated with a 97% specificity for advanced fibrosis — "
            "meaning this result is unlikely to be a false alarm, and it "
            "should be taken seriously."
        ),
        "action_heading": "What to do next",
        "action_low": (
            "Lifestyle counselling (diet, exercise, weight management). "
            "Repeat this test in 1–2 years, or sooner if you develop new "
            "risk factors like diabetes or significant weight gain."
        ),
        "action_intermediate": (
            "Share this result with your GP or family doctor. They may "
            "recommend a FibroScan (transient elastography) or other "
            "follow-up test to clarify your fibrosis risk."
        ),
        "action_high": (
            "Please arrange to see a hepatologist (liver specialist) or "
            "gastroenterologist soon. Bring this result and your original "
            "blood report with you."
        ),
        "bmi_context_heading": "Your BMI context",
        "bmi_underweight": "Underweight",
        "bmi_normal": "Normal range",
        "bmi_overweight": "Overweight",
        "bmi_obese": "Obese",
        "bmi_note": (
            "Obesity and a high BMI are among the strongest known risk "
            "factors for NAFLD, independent of your FIB-4 score."
        ),
        "diabetes_note": (
            "Diabetes and pre-diabetes significantly increase both the risk "
            "of NAFLD and the risk of it progressing to more serious liver "
            "damage. This makes regular monitoring more important."
        ),
        "family_history_note": (
            "A family history of fatty liver disease or metabolic syndrome "
            "increases your own risk. It's worth mentioning to your doctor "
            "even if your FIB-4 score is low."
        ),
        "age_warning": (
            "⚠️ FIB-4 has been clinically validated primarily for adults "
            "aged 35–65. Outside this age range, the score is less "
            "reliable and may produce more false positives or false "
            "negatives. Please discuss this result with a doctor rather "
            "than relying on it alone."
        ),
        "disclaimer_heading": "Important — please read",
        "disclaimer_body": (
            "**This is a screening tool, not a diagnosis.** FIB-4 is a "
            "statistical estimate based on published research, not a "
            "medical test performed on you directly. It does not measure "
            "liver fat (steatosis) — only fibrosis (scarring) risk. "
            "Intermediate or High risk results require confirmation by a "
            "qualified medical professional, potentially using additional "
            "tests such as FibroScan. LivrCheck and its creator are not "
            "responsible for medical decisions made based on this tool. "
            "When in doubt, consult a doctor."
        ),
        "formula_heading": "How this is calculated",
        "formula_body": (
            "FIB-4 = (Age × AST) ÷ (Platelet count × √ALT)\n\n"
            "Source: Sterling RK, et al. *Hepatology*. 2006;43:1317. "
            "This formula is widely used in Indian hospitals and is "
            "endorsed as a first-line fibrosis screening approach in "
            "resource-limited settings."
        ),
        "share_heading": "Share this with your family",
        "share_body": (
            "If this was useful, share LivrCheck with a family member. "
            "NAFLD often runs in families, and early detection matters most "
            "in the reversible stages."
        ),
        "share_button_text": "Share on WhatsApp",
        "share_message_template": (
            "I just checked my liver fibrosis risk using LivrCheck, a free "
            "tool built from clinically validated research. It only takes "
            "a routine blood test. You should check yours too: {url}"
        ),
        "print_button": "Download my result card",
        "footer_note": (
            "LivrCheck is a free, open-source, non-commercial screening "
            "tool. It does not store or transmit your data anywhere."
        ),
        "validation_error": "Please enter valid, positive numbers for all fields.",
        "result_card_title": "LivrCheck Result Card",
        "result_card_generated": "Generated on",
    },
    "hi": {
        # NEEDS_NATIVE_REVIEW: draft translation, not yet checked by a
        # native Hindi speaker.
        "app_title": "लिवरचेक",
        "app_subtitle": "एक सामान्य ब्लड टेस्ट से अपने लिवर फाइब्रोसिस जोखिम को जानें",
        "language_label": "भाषा / Language",
        "intro_heading": "यह टूल क्या है?",
        "intro_body": (
            "लिवरचेक आपका **FIB-4 स्कोर** निकालता है, जो लिवर फाइब्रोसिस "
            "(लिवर में घाव के निशान) के जोखिम का एक चिकित्सकीय रूप से "
            "मान्य अनुमान है। इसके लिए एक सामान्य ब्लड टेस्ट के चार आंकड़े "
            "चाहिए: आपकी उम्र, AST, ALT, और प्लेटलेट काउंट। ये आंकड़े एक "
            "सामान्य Liver Function Test (LFT) और Complete Blood Count "
            "(CBC) रिपोर्ट में मिलते हैं — जो कई परिवारों के पास पहले से "
            "ही किसी दराज में रखी होती है।"
        ),
        "not_alcohol_heading": "इसका शराब से कोई संबंध नहीं है",
        "not_alcohol_body": (
            "Non-Alcoholic Fatty Liver Disease (NAFLD) खान-पान, मोटापा, "
            "डायबिटीज़ और शारीरिक निष्क्रियता की वजह से होता है — शराब "
            "की वजह से नहीं। कई भारतीय परिवार फैटी लिवर की जांच को शराब "
            "की समस्या समझ लेते हैं, जिससे सही जांच और इलाज में वर्षों की "
            "देरी हो सकती है।"
        ),
        "form_heading": "अपने ब्लड टेस्ट के आंकड़े दर्ज करें",
        "age_label": "उम्र (वर्ष)",
        "ast_label": "AST (U/L)",
        "ast_help": "रिपोर्ट में कभी-कभी SGOT लिखा होता है",
        "alt_label": "ALT (U/L)",
        "alt_help": "रिपोर्ट में कभी-कभी SGPT लिखा होता है",
        "platelets_label": "प्लेटलेट काउंट (×10⁹/L, यानी लाख/cmm × 100)",
        "platelets_help": (
            "यदि आपकी रिपोर्ट में प्लेटलेट्स लाख/cmm में हैं (जैसे 2.5 "
            "लाख/cmm), तो ×10⁹/L पाने के लिए 100 से गुणा करें (जैसे 2.5 → 250)।"
        ),
        "context_heading": "कुछ और सवाल (वैकल्पिक, पर उपयोगी जानकारी के लिए)",
        "bmi_heading": "बॉडी मास इंडेक्स (BMI)",
        "height_label": "लंबाई (सेमी)",
        "weight_label": "वज़न (किलो)",
        "diabetes_label": "क्या आपको डायबिटीज़ या प्री-डायबिटीज़ है?",
        "family_history_label": (
            "क्या आपके परिवार में किसी को फैटी लिवर, सिरोसिस, या मेटाबॉलिक "
            "सिंड्रोम (डायबिटीज़ + मोटापा + हाई बीपी) है?"
        ),
        "yes": "हाँ",
        "no": "नहीं",
        "not_sure": "पता नहीं",
        "calculate_button": "मेरा FIB-4 स्कोर निकालें",
        "results_heading": "आपके परिणाम",
        "score_label": "FIB-4 स्कोर",
        "tier_low": "कम जोखिम",
        "tier_intermediate": "मध्यम जोखिम",
        "tier_high": "उच्च जोखिम",
        "tier_low_explanation": (
            "आपका स्कोर दर्शाता है कि गंभीर लिवर फाइब्रोसिस की संभावना कम "
            "है। शोध के अनुसार, इस स्तर का स्कोर लगभग 91% मामलों में सही "
            "साबित होता है (negative predictive value ~90.7%)।"
        ),
        "tier_intermediate_explanation": (
            "आपका स्कोर मध्यम श्रेणी में है। इसका मतलब यह नहीं कि "
            "फाइब्रोसिस है, पर इसे पूरी तरह खारिज भी नहीं किया जा सकता। "
            "आगे की जांच की सलाह दी जाती है।"
        ),
        "tier_high_explanation": (
            "आपका स्कोर उच्च-जोखिम सीमा से ऊपर है। 3.25 से ऊपर के स्कोर "
            "गंभीर फाइब्रोसिस के लिए 97% विशिष्टता (specificity) रखते हैं "
            "— यानी यह परिणाम गलत अलार्म होने की संभावना कम है, और इसे "
            "गंभीरता से लेना चाहिए।"
        ),
        "action_heading": "आगे क्या करें",
        "action_low": (
            "जीवनशैली परामर्श (खान-पान, व्यायाम, वज़न नियंत्रण)। यह टेस्ट "
            "1–2 साल में दोबारा करवाएं, या जल्दी अगर डायबिटीज़ जैसी नई "
            "समस्या हो या वज़न काफी बढ़ जाए।"
        ),
        "action_intermediate": (
            "यह परिणाम अपने डॉक्टर के साथ साझा करें। वे FibroScan "
            "(transient elastography) या अन्य जांच की सलाह दे सकते हैं।"
        ),
        "action_high": (
            "कृपया जल्द ही किसी हेपेटोलॉजिस्ट (लिवर विशेषज्ञ) या "
            "गैस्ट्रोएंटेरोलॉजिस्ट से मिलें। यह परिणाम और अपनी मूल ब्लड "
            "रिपोर्ट साथ लेकर जाएं।"
        ),
        "bmi_context_heading": "आपका BMI संदर्भ",
        "bmi_underweight": "कम वज़न",
        "bmi_normal": "सामान्य",
        "bmi_overweight": "अधिक वज़न",
        "bmi_obese": "मोटापा",
        "bmi_note": (
            "मोटापा और उच्च BMI, आपके FIB-4 स्कोर से अलग, NAFLD के सबसे "
            "बड़े जोखिम कारकों में से हैं।"
        ),
        "diabetes_note": (
            "डायबिटीज़ और प्री-डायबिटीज़, NAFLD होने और उसके गंभीर लिवर "
            "क्षति में बदलने, दोनों के जोखिम को काफी बढ़ा देते हैं। इसलिए "
            "नियमित जांच ज़रूरी है।"
        ),
        "family_history_note": (
            "परिवार में फैटी लिवर या मेटाबॉलिक सिंड्रोम का इतिहास आपके "
            "अपने जोखिम को बढ़ाता है। अपने FIB-4 स्कोर के कम होने पर भी "
            "यह जानकारी डॉक्टर को बताना उपयोगी है।"
        ),
        "age_warning": (
            "⚠️ FIB-4 मुख्य रूप से 35–65 वर्ष के वयस्कों के लिए मान्य "
            "किया गया है। इस उम्र सीमा के बाहर, स्कोर की विश्वसनीयता कम "
            "हो जाती है और गलत परिणाम आने की संभावना बढ़ जाती है। कृपया "
            "इस परिणाम पर पूरी तरह भरोसा करने के बजाय डॉक्टर से चर्चा करें।"
        ),
        "disclaimer_heading": "ज़रूरी सूचना — कृपया पढ़ें",
        "disclaimer_body": (
            "**यह एक स्क्रीनिंग टूल है, निदान (diagnosis) नहीं है।** "
            "FIB-4 प्रकाशित शोध पर आधारित एक सांख्यिकीय अनुमान है, न कि "
            "आप पर सीधे किया गया चिकित्सा परीक्षण। यह लिवर में वसा "
            "(steatosis) को नहीं मापता — केवल फाइब्रोसिस (घाव) के जोखिम "
            "को मापता है। मध्यम या उच्च जोखिम वाले परिणामों की पुष्टि "
            "किसी योग्य चिकित्सक द्वारा, संभवतः FibroScan जैसी अतिरिक्त "
            "जांच से करवाना ज़रूरी है। लिवरचेक और इसके निर्माता इस टूल के "
            "आधार पर लिए गए किसी भी चिकित्सा निर्णय के लिए ज़िम्मेदार नहीं "
            "हैं। संदेह होने पर डॉक्टर से सलाह लें।"
        ),
        "formula_heading": "यह कैसे निकाला जाता है",
        "formula_body": (
            "FIB-4 = (उम्र × AST) ÷ (प्लेटलेट काउंट × √ALT)\n\n"
            "स्रोत: Sterling RK, et al. *Hepatology*. 2006;43:1317. यह "
            "फॉर्मूला भारतीय अस्पतालों में व्यापक रूप से उपयोग होता है।"
        ),
        "share_heading": "अपने परिवार के साथ साझा करें",
        "share_body": (
            "अगर यह उपयोगी लगा, तो लिवरचेक अपने परिवार के सदस्यों के साथ "
            "साझा करें। NAFLD अक्सर परिवारों में चलता है, और जल्दी पहचान "
            "उस चरण में सबसे ज़्यादा मायने रखती है जब यह अभी ठीक हो सकता है।"
        ),
        "share_button_text": "व्हाट्सएप पर साझा करें",
        "share_message_template": (
            "मैंने अभी लिवरचेक से अपना लिवर फाइब्रोसिस जोखिम जांचा — यह एक "
            "मुफ़्त टूल है जो मान्य शोध पर आधारित है। इसके लिए बस एक "
            "सामान्य ब्लड टेस्ट चाहिए। आप भी अपना जांच लें: {url}"
        ),
        "print_button": "मेरा रिज़ल्ट कार्ड डाउनलोड करें",
        "footer_note": (
            "लिवरचेक एक मुफ़्त, ओपन-सोर्स, गैर-व्यावसायिक स्क्रीनिंग टूल "
            "है। यह आपका डेटा कहीं भी संग्रहीत या प्रसारित नहीं करता।"
        ),
        "validation_error": "कृपया सभी फ़ील्ड में सही, धनात्मक संख्याएं दर्ज करें।",
        "result_card_title": "लिवरचेक रिज़ल्ट कार्ड",
        "result_card_generated": "बनाया गया",
    },
}


def t(lang: str, key: str) -> str:
    """Fetch a translated string, falling back to English if missing."""
    return TEXT.get(lang, TEXT["en"]).get(key, TEXT["en"].get(key, key))

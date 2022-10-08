from os import link
import linkFunctions

def test_usefulLinks():
    assert linkFunctions.browseInCollege() == "\nUnder construction"
    assert linkFunctions.businessSolutions() == "\nUnder construction"
    assert linkFunctions.directories() == "\nUnder construction"
    assert linkFunctions.helpCenter() == "\nWe're here to help"
    assert linkFunctions.aboutUseful() == "\nIn College: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide"
    assert linkFunctions.press() == "\nIn College Pressroom: Stay on top of the latest news, updates,and reports"
    assert linkFunctions.blog() == "\nUnder construction"
    assert linkFunctions.careers() == "\nUnder construction"
    assert linkFunctions.developers() == "\nUnder construction"

def test_importantLinks():
    assert linkFunctions.copyrightNotice() == "\n© InCollege Corporation 2022. All Rights Reserved."
    assert linkFunctions.aboutImportant() == "\nAbout InCollege\nWelcome to InCollege website, the world's largest professional network for all college students!"
    assert linkFunctions.accessibility() == "\nInCollege is a place where every student can find their opportunity. Whatever your goals, ideas, and abilities are, we're here to help you succeed."
    assert linkFunctions.userAgreement() == "\nWhen you use our services you agree to all of these terms. Your use of our services is also subject to our cookie policy and our privacy policy, which covers how we collect, use, share, and store your personal information. Please see the detail. "
    assert linkFunctions.cookiePolicy() == "\nAt InCollege, cookie can be used to recognized you when you visit InCollege, remember your preferences, and give you a personalized experience that's in line with your setting. Cookies make your interations with InCollege faster and more secure."
    assert linkFunctions.copyrightPolicy() == "\nYou may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to others without obtaining the prior written consent of the owner of such proprietary rights."
    assert linkFunctions.brandPolicy() == "\nOur trademarks and other brand features are protected by law.  You’ll need our permission in order to use them."
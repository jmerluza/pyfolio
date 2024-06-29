# =================================================================================================
# LINKEDIN PROFILE BADGE
# =================================================================================================
# 1. Go to this link: https://www.linkedin.com/pulse/how-create-linkedin-badge-your-website-amy-wallin/
# 2. Follow the steps in the above link until you get to the public profile badge builder page.
# 3. Copy the js script that linkedin provides and paste into the linkedin_js variable below.
# 4. Copy the html script for the badge option you like and paste into the linkedin_html variable below.

linkedin_js = '<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>'
linkedin_html = """
<div 
    class="badge-base LI-profile-badge" 
    data-locale="en_US" 
    data-size="medium" 
    data-theme="dark" 
    data-type="VERTICAL" 
    data-vanity="jalen-merluza-30b33916b" 
    data-version="v1"
>
    <a 
        class="badge-base__link LI-simple-link" 
        href="https://ca.linkedin.com/in/jalen-merluza-30b33916b?trk=profile-badge">
    </a>
</div>
"""
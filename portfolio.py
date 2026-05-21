import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Monika Jaiswal | Portfolio",
    page_icon="💼",
    layout="wide"
)

# Professional Linear Gradient CSS
st.markdown("""
<style>
    /* Reset & Base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main Background - Soft Linear Gradient */
    .stApp {
        background: linear-gradient(135deg, #F0F4FF 0%, #E8EEFF 50%, #FFFFFF 100%);
    }
    
    /* Container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Header Section - Blue Gradient */
    .header {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #1E3A8A 100%);
        border-radius: 15px;
        padding: 40px;
        margin-bottom: 30px;
        color: white;
    }
    
    .name {
        font-size: 48px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }
    
    .title {
        font-size: 20px;
        color: #DBEAFE;
        margin-bottom: 15px;
    }
    
    .location {
        color: #BFDBFE;
        margin-bottom: 20px;
    }
    
    /* Button Styles */
    .btn-blue {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
        margin-right: 15px;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .btn-blue:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    
    .btn-red {
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .btn-red:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(220,38,38,0.3);
    }
    
    .btn-outline {
        background: transparent;
        color: #1E3A8A;
        padding: 10px 25px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        font-weight: 600;
        border: 2px solid #1E3A8A;
        transition: all 0.3s;
    }
    
    .btn-outline:hover {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white;
        border-color: transparent;
    }
    
    /* Section Title */
    .section-title {
        font-size: 28px;
        font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #DC2626 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #DC2626;
        display: inline-block;
    }
    
    /* Card Styles - White with Soft Shadow */
    .card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s;
    }
    
    .card:hover {
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    /* Stat Box */
    .stat-box {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0F4FF 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border-top: 3px solid #1E3A8A;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #4B5563;
        margin-top: 5px;
    }
    
    /* Education Card */
    .edu-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border-left: 4px solid #DC2626;
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    
    .edu-title {
        font-size: 18px;
        font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    /* Skill Badge */
    .skill-badge {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
        transition: all 0.3s;
    }
    
    .skill-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    
    /* Service Card */
    .service-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .service-card:hover {
        border-color: #2563EB;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    
    .service-price {
        font-size: 24px;
        font-weight: 700;
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
    }
    
    /* Project Card */
    .project-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .project-card:hover {
        border-color: #DC2626;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    
    .project-tech {
        color: #DC2626;
        font-size: 13px;
        margin: 8px 0;
    }
    
    /* Contact Info */
    .contact-item {
        padding: 12px;
        border-bottom: 1px solid rgba(37,99,235,0.1);
        color: #1F2937;
    }
    
    .contact-item strong {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        color: #9CA3AF;
        padding: 30px;
        text-align: center;
        border-radius: 12px;
        margin-top: 40px;
    }
    
    hr {
        margin: 20px 0;
        border: none;
        border-top: 1px solid rgba(37,99,235,0.2);
    }
    
    /* Text Colors */
    .text-gradient-blue {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .text-gradient-red {
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER SECTION ====================
st.markdown("""
<div class="header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div class="name">Monika Jaiswal</div>
            <div class="title">💻 Computer Science Student | Software Developer | Freelancer</div>
            <div class="location">📍 India | Available for Remote Work</div>
            <div style="margin-top: 20px;">
                <button class="btn-blue" onclick="alert('Contact: monikajaiswal200@gmail.com')">📞 Hire Me</button>
                <button class="btn-red" onclick="alert('Resume download link will be shared')">📄 Download Resume</button>
            </div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 80px;">👩‍💻</div>
            <div style="background-color: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; margin-top: 10px;">
                🔥 Open for Work
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== STATS SECTION ====================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">3</div>
        <div class="stat-label">🎓 Qualifications</div>
        <small>Polytechnic + BCA + MCA</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">50+</div>
        <div class="stat-label">💻 Projects</div>
        <small>Successfully Completed</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">20+</div>
        <div class="stat-label">🤝 Happy Clients</div>
        <small>Worldwide</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">100%</div>
        <div class="stat-label">⭐ Satisfaction</div>
        <small>5 Star Rating</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== ABOUT SECTION ====================
st.markdown('<h2 class="section-title">📖 About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card">
        <p style="font-size: 16px; line-height: 1.6;">
            Hello! I'm <strong class="text-gradient-blue">Monika Jaiswal</strong>, a passionate Computer Science student 
            with a strong foundation in programming and web development.
        </p>
        <p style="margin-top: 15px;">
        <strong class="text-gradient-red">🎯 My Journey:</strong><br>
        ✓ <strong>Polytechnic (CS)</strong> - Started my coding journey<br>
        ✓ <strong>BCA</strong> - Completed with 85%<br>
        ✓ <strong>MCA (Current)</strong> - Pursuing to master advanced concepts<br>
        ✓ <strong>Freelancer</strong> - Helping clients since 2021
        </p>
        <p style="margin-top: 15px;">
        <strong class="text-gradient-red">💡 What I Offer:</strong><br>
        ✓ Clean, professional code with documentation<br>
        ✓ Timely delivery with regular updates<br>
        ✓ Affordable rates for students & startups<br>
        ✓ Post-delivery support
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <div style="font-size: 60px;">👩‍🎓</div>
        <h3 class="text-gradient-blue">Monika Jaiswal</h3>
        <p>CS Student & Developer</p>
        <hr>
        <div style="text-align: left;">
            <p>📧 <strong>monikajaiswal200@gmail.com</strong></p>
            <p>📱 <strong>+91 8736019810</strong></p>
            <p>📍 <strong>India</strong></p>
        </div>
        <hr>
        <p>⭐⭐⭐⭐⭐<br><small>Rated 5/5 by clients</small></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== EDUCATION SECTION ====================
st.markdown('<h2 class="section-title">🎓 Education</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="edu-card">
        <div class="edu-title">🎓 Master of Computer Applications (MCA)</div>
        <p><strong>2023 - 2025 | Current Student</strong></p>
        <p>• CGPA: 8.7/10<br>• Specialization: Full Stack Development<br>• Current Semester: 3rd</p>
    </div>
    <div class="edu-card">
        <div class="edu-title">📘 Bachelor of Computer Applications (BCA)</div>
        <p><strong>2020 - 2023 | Completed</strong></p>
        <p>• Percentage: 85%<br>• University Rank: Top 15<br>• Best Project Award</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="edu-card">
        <div class="edu-title">💻 Diploma in Computer Science (Polytechnic)</div>
        <p><strong>2017 - 2020 | Completed</strong></p>
        <p>• Percentage: 82%<br>• Specialized in Programming<br>• Foundation of coding</p>
    </div>
    <div class="card">
        <div class="edu-title" style="font-size: 16px;">📜 Certifications</div>
        <p>✓ Python for Everybody - Coursera<br>✓ Web Development Bootcamp - Udemy<br>✓ Database Management - NPTEL<br>✓ React Complete Guide</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== SKILLS SECTION ====================
st.markdown('<h2 class="section-title">⚡ Technical Skills</h2>', unsafe_allow_html=True)

skills = ["Python", "JavaScript", "Java", "C++", "React", "Django", 
          "Flask", "MySQL", "MongoDB", "Git", "HTML/CSS", "Bootstrap",
          "REST API", "Pandas", "NumPy", "Docker"]

# Display skills in rows
for i in range(0, len(skills), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(skills):
            with cols[j]:
                st.markdown(f'<div class="skill-badge">{skills[i + j]}</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== SERVICES SECTION ====================
st.markdown('<h2 class="section-title">💼 Freelance Services</h2>', unsafe_allow_html=True)

services = [
    {"icon": "🐍", "name": "Python Development", "price": "₹4,999", "desc": "Automation, Scripts, APIs"},
    {"icon": "🌐", "name": "Web Development", "price": "₹7,999", "desc": "Responsive Websites"},
    {"icon": "📱", "name": "Web Applications", "price": "₹12,999", "desc": "Full-Stack Apps"},
    {"icon": "🗄️", "name": "Database Design", "price": "₹3,999", "desc": "Optimization & Queries"},
    {"icon": "🤖", "name": "Chatbot Development", "price": "₹5,999", "desc": "AI Powered Chatbots"},
    {"icon": "📊", "name": "Data Analysis", "price": "₹4,999", "desc": "Visualization & Reports"}
]

service_cols = st.columns(3)
for i, service in enumerate(services):
    with service_cols[i % 3]:
        st.markdown(f"""
        <div class="service-card">
            <div style="font-size: 40px;">{service['icon']}</div>
            <h3 class="text-gradient-blue">{service['name']}</h3>
            <div class="service-price">{service['price']}</div>
            <p style="color: #6B7280;">{service['desc']}</p>
            <button class="btn-outline" style="padding: 6px 15px; font-size: 13px; width: 100%;" 
                    onclick="alert('Contact monikajaiswal200@gmail.com for {service['name']}')">
                Get Quote →
            </button>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== PROJECTS SECTION ====================
st.markdown('<h2 class="section-title">🚀 My Projects</h2>', unsafe_allow_html=True)

projects = [
    {"name": "E-Learning Platform", "tech": "Django, React, PostgreSQL", "desc": "Online learning with video lectures, quizzes & certificates"},
    {"name": "College Management System", "tech": "Python, MySQL", "desc": "Manage student records, fees, attendance"},
    {"name": "Portfolio Generator", "tech": "Streamlit, Python", "desc": "Create professional portfolios in minutes"},
    {"name": "Chatbot Assistant", "tech": "Python, NLP, Flask", "desc": "AI-powered customer support chatbot"},
    {"name": "Freelance Manager", "tech": "Flask, MongoDB", "desc": "Manage projects, clients & payments"},
    {"name": "Data Dashboard", "tech": "Streamlit, Pandas", "desc": "Interactive data visualization dashboard"}
]

project_cols = st.columns(3)
for i, project in enumerate(projects):
    with project_cols[i % 3]:
        st.markdown(f"""
        <div class="project-card">
            <div style="font-size: 24px; margin-bottom: 10px;">📁</div>
            <h4 class="text-gradient-blue">{project['name']}</h4>
            <div class="project-tech">{project['tech']}</div>
            <p style="color: #6B7280; font-size: 14px;">{project['desc']}</p>
            <button class="btn-outline" style="padding: 4px 12px; font-size: 12px;">View Details →</button>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== WHY HIRE ME ====================
st.markdown('<h2 class="section-title">✨ Why Choose Me?</h2>', unsafe_allow_html=True)

why_cols = st.columns(4)

why_data = [
    {"icon": "✅", "title": "Quality Work", "desc": "Clean, documented code"},
    {"icon": "⚡", "title": "Fast Delivery", "desc": "On-time delivery"},
    {"icon": "💰", "title": "Affordable", "desc": "Student friendly rates"},
    {"icon": "💬", "title": "24/7 Support", "desc": "Always available"}
]

for i, item in enumerate(why_data):
    with why_cols[i]:
        st.markdown(f"""
        <div class="stat-box" style="height: 100%;">
            <div style="font-size: 32px;">{item['icon']}</div>
            <div class="stat-number" style="font-size: 20px;">{item['title']}</div>
            <div class="stat-label">{item['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== CONTACT SECTION ====================
st.markdown('<h2 class="section-title">📬 Contact Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3 class="text-gradient-blue">📞 Get in Touch</h3>
        <div class="contact-item">
            📧 <strong>Email:</strong> monikajaiswal200@gmail.com
        </div>
        <div class="contact-item">
            📱 <strong>Phone:</strong> +91 8736019810
        </div>
        <div class="contact-item">
            💬 <strong>WhatsApp:</strong> Available
        </div>
        <div class="contact-item">
            🌍 <strong>Location:</strong> India (Remote)
        </div>
        <hr>
        <h3 class="text-gradient-red">🌐 Find Me On</h3>
        <div class="contact-item">
            🔗 <strong>LinkedIn:</strong> /in/monika-jaiswal<br>
            🐙 <strong>GitHub:</strong> /monikajaiswal<br>
            📸 <strong>Instagram:</strong> @monika_codes
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.markdown("### ✉️ Send a Message")
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email")
        service_interest = st.selectbox("I'm interested in", 
                                        ["Python Development", "Web Development", "Web App", 
                                         "Database Design", "Chatbot", "Data Analysis"])
        message = st.text_area("Message", placeholder="Tell me about your project...", height=100)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            st.success("✅ Message sent! I'll reply within 24 hours.")
            st.balloons()

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <p>© 2024 Monika Jaiswal | Computer Science Student & Software Developer</p>
    <p>💼 Available for Freelance Work | Let's Build Something Great Together</p>
    <p style="margin-top: 10px;">📧 monikajaiswal200@gmail.com | 📱 +91 8736019810</p>
</div>
""", unsafe_allow_html=True)
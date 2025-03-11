from shiny import App, ui

# Define the UI
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            "📬 Contact Information",
            ui.h2("Contact Information"),
            ui.p("Name: William Chupp"),
            ui.p("Email: billychupp94@gmail.com"),
            ui.p("Phone: 203-868-9205"),
            ui.p("Location: 412 Norfolk St., Cambridge, MA, 02139"),
        ),
        ui.navset_bar(
            # Profile Tab
            ui.nav_panel(
                "🌟 Profile",
                ui.h2("Profile"),
                ui.p(
                    """
                    🚀 Engineer, data scientist, researcher, and project manager in the environmental 
                    and air quality fields with a passion for transportation and public service.
                    """
                ),
                ui.p(
                    """
                    🔧 Eight years of experience working on federal projects across various domains, 
                    including EPA’s MOVES model, environmental modeling, and large-scale data analysis.
                    """
                ),
                ui.p(
                    """
                    💡 Enjoy working with large datasets, generating visualizations, creating tools, 
                    and delivering actionable insights to stakeholders.
                    """
                ),
            ),
            # Work Experience Tab
            ui.nav_panel(
                "💼 Work Experience",
                ui.h2("Work Experience"),
                ui.h3("Engineer, Volpe Transportation Systems Center – US Department of Transportation"),
                ui.p("2016 – Present, Cambridge MA"),
                ui.markdown(
                    """
                    ⚙️ Managed teams to deliver software tools, web applications, visualizations, and data analysis results.
                    🌍 Focused on air quality and transportation’s environmental impact.
                    🗂️ Built large databases using SQL and analyzed data using Python.
                    📚 Published findings in peer-reviewed journals and presented at conferences.
                    """
                ),
                ui.h3("Service and Assembly, Belmont WheelWorks"),
                ui.p("Summer 2015, Belmont MA"),
                ui.markdown(
                    """
                    🚴 Built and repaired bicycles full-time in a retail bike store.
                    🛠️ Assisted in everyday business operations.
                    """
                ),
                ui.h3("Engineering Intern, The Lee Company"),
                ui.p("Summer 2014, Westbrook CT"),
                ui.markdown(
                    """
                    🔬 Conducted product testing, research, and development for microfluidic components.
                    📊 Presented results to lead and project engineers.
                    """
                ),
            ),
            # Education Tab
            ui.nav_panel(
                "🎓 Education",
                ui.h2("Education"),
                ui.h3("Master of Engineering in Mechanical Engineering"),
                ui.p("Tufts University, Medford, MA – May 2018"),
                ui.h3("Bachelor of Science in Mechanical Engineering"),
                ui.p("Tufts University, Medford, MA – May 2017"),
                ui.p("🎖️ Honors: Graduated Magna Cum Laude, Dean’s List all semesters."),
            ),
            # Skills Tab
            ui.nav_panel(
                "🛠️ Skills",
                ui.h2("Skills"),
                ui.h3("Programming"),
                ui.markdown(
                    """
                    - Python (Expert)
                    - SQL (Expert)
                    - VBA (Expert)
                    """
                ),
                ui.h3("Tools"),
                ui.markdown(
                    """
                    - EPA’s MOVES (Expert)")
                    - Microsoft Office (Expert)
                    - Web and Cloud Development (Working)
                    """
                ),
                ui.h3("Management"),
                ui.markdown(
                    """
                    - Project Management (Expert)
                    - Business Development (Expert)
                    - Customer Service (Expert)
                    - Strategic Planning (Expert)
                    """
                ),
            ),
            # Projects Tab
            ui.nav_panel(
                "📂 Projects",
                ui.h2("Projects"),
                ui.h3("Transportation Air Quality Analysis Web Application Toolkit"),
                ui.p(
                    """
                    - 🛠️ Led development of the CMAQ Emissions Calculator Toolkit to build web applications 
                    from spreadsheet-based tools.
                    """
                ),
                ui.p(
                    """
                    - 🌐 Developed tools for practitioners to estimate emissions reductions from transportation 
                    infrastructure projects.
                    """
                ),
                ui.h3("Earthquake and Traffic Safety Research and Analysis"),
                ui.p(
                    """
                    - 📊 Quantified traffic safety impacts using police-reported and crowd-sourced crash reports.
                    """
                ),
                ui.h3("Voice Controlled Robotics Applications for In-Home Assistance"),
                ui.p(
                    """
                    - 🤖 Designed a system to assist people with spinal cord injuries using Python-controlled robotics.
                    """
                ),
            ),
            # Personal Interests Tab
            ui.nav_panel(
                "🎯 Personal Interests",
                ui.h2("Personal Interests"),
                ui.p(
                    """
                    🏂 Snowboarding, 🎿 Backcountry Skiing, 🏃 Running, 🚴 Cycling, 🚵 Gravel Biking, 🥾 Hiking, 
                    🎒 Backpacking, 🍳 Cooking, 🎵 Music, 🛼 Rollerblading, 🏉 Rugby, 🎺 Playing Tuba.
                    """
                ),
            ),
            title='About Me'
        )
    )
)


# Define the server logic
def server(input, output, session):
    pass  # No server-side logic needed for static content

# Create the app
app = App(app_ui, server)

# # Contact Tab
#         ui.nav_panel(
#             "📬 Contact Information",
#             ui.h2("Contact Information"),
#             ui.p("Name: William Chupp"),
#             ui.p("Email: billychupp94@gmail.com"),
#             ui.p("Phone: 203-868-9205"),
#             ui.p("Location: 412 Norfolk St., Cambridge, MA, 02139"),
#         ),
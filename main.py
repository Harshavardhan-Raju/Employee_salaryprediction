import streamlit as st
import json

# Set page configuration
st.set_page_config(page_title="Developer Survey", page_icon="💻", layout="wide")

# Title
st.title("🔍 Developer Survey")
st.markdown("---")

# Initialize session state for form data
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Job Description - Single Select
st.header("Current Job Description")
job_options = [
    "Academic researcher",
    "Blockchain",
    "Cloud infrastructure engineer",
    "Data or business analyst",
    "Data engineer",
    "Data scientist or machine learning specialist",
    "Database administrator",
    "Designer",
    "Developer Advocate",
    "Developer, AI",
    "Developer, back-end",
    "Developer, desktop or enterprise applications",
    "Developer, embedded applications or devices",
    "Developer Experience",
    "Developer, front-end",
    "Developer, full-stack",
    "Developer, game or graphics",
    "Developer, mobile",
    "Developer, QA or test",
    "DevOps specialist",
    "Educator",
    "Engineer, site reliability",
    "Engineering manager",
    "Hardware Engineer",
    "Marketing or sales professional",
    "Product manager",
    "Project manager",
    "Research & Development role",
    "Scientist",
    "Senior Executive (C-Suite, VP, etc.)",
    "Student",
    "System administrator",
    "Security professional",
    "Other"
]

current_job = st.selectbox(
    "Which of the following describes your current job, the one you do most of the time? Please select only one.",
    ["Select an option"] + job_options
)

# Education Level - Single Select
st.header("Education Level")
education_options = [
    "Primary/elementary school",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
    "Some college/university study without earning a degree",
    "Associate degree (A.A., A.S., etc.)",
    "Bachelor's degree (B.A., B.S., B.Eng., etc.)",
    "Master's degree (M.A., M.S., M.Eng., MBA, etc.)",
    "Professional degree (JD, MD, Ph.D, Ed.D, etc.)",
    "Something else"
]

education = st.selectbox(
    "Which of the following best describes the highest level of formal education that you've completed?",
    ["Select an option"] + education_options
)

# Age - Single Select
st.header("Age")
age_options = [
    "Under 18 years old",
    "18-24 years old",
    "25-34 years old",
    "35-44 years old",
    "45-54 years old",
    "55-64 years old",
    "65 years or older",
    "Prefer not to say"
]

age = st.selectbox("What is your age?", ["Select an option"] + age_options)

# Employment Status - Multi Select
st.header("Employment Status")
employment_options = [
    "Employed, full-time",
    "Employed, part-time",
    "Independent contractor, freelancer, or self-employed",
    "Not employed, but looking for work",
    "Not employed, and not looking for work",
    "Student, full-time",
    "Student, part-time",
    "Retired",
    "I prefer not to say"
]

employment_status = st.multiselect(
    "Which of the following best describes your current employment status? Select all that apply.",
    employment_options
)

# Work Situation - Single Select
st.header("Work Situation")
work_situation_options = ["Remote", "In-person", "Hybrid (some remote, some in-person)"]
work_situation = st.selectbox(
    "Which best describes your current work situation?",
    ["Select an option"] + work_situation_options
)

# Programming Languages - Multi Select
st.header("Programming Languages")
programming_languages = [
    "Ada", "Apex", "Assembly", "Bash/Shell (all shells)", "C", "C#", "C++", "Clojure", "Cobol", "Crystal",
    "Dart", "Delphi", "Elixir", "Erlang", "F#", "Fortran", "GDScript", "Go", "Groovy", "Haskell",
    "HTML/CSS", "Java", "JavaScript", "Julia", "Kotlin", "Lisp", "Lua", "MATLAB", "MicroPython", "Nim",
    "Objective-C", "OCaml", "Perl", "PHP", "PowerShell", "Prolog", "Python", "R", "Ruby", "Rust",
    "Scala", "Solidity", "SQL", "Swift", "TypeScript", "VBA", "Visual Basic (.Net)", "Zephyr", "Zig"
]

selected_languages = st.multiselect(
    "Which programming, scripting, and markup languages have you worked with?",
    programming_languages
)

# Database Environments - Multi Select
st.header("Database Environments")
databases = [
    "BigQuery", "Cassandra", "Clickhouse", "Cloud Firestore", "Cockroachdb", "Cosmos DB", "Couch DB",
    "Couchbase", "Databricks SQL", "Datomic", "DuckDB", "Dynamodb", "Elasticsearch", "EventStoreDB",
    "Firebase Realtime Database", "Firebird", "H2", "IBM DB2", "InfluxDB", "MariaDB", "Microsoft Access",
    "Microsoft SQL Server", "MongoDB", "MySQL", "Neo4J", "Oracle", "PostgreSQL", "Presto", "RavenDB",
    "Redis", "Snowflake", "Solr", "SQLite", "Supabase", "TiDB"
]

selected_databases = st.multiselect(
    "Which database environments have you worked with?",
    databases
)

# Cloud Platforms - Multi Select
st.header("Cloud Platforms")
cloud_platforms = [
    "Alibaba Cloud", "Amazon Web Services (AWS)", "Cloudflare", "Colocation", "Databricks", "Digital Ocean",
    "Firebase", "Fly.io", "Google Cloud", "Heroku", "Hetzner", "IBM Cloud Or Watson", "Linode",
    "Managed Hosting", "Microsoft Azure", "Netlify", "OpenShift", "OpenStack", "Oracle Cloud Infrastructure (OCI)",
    "OVH", "PythonAnywhere", "Render", "Scaleway", "Supabase", "Vercel", "VMware", "Vultr"
]

selected_cloud = st.multiselect(
    "Which cloud platforms have you worked with?",
    cloud_platforms
)

# Web Frameworks - Multi Select
st.header("Web Frameworks and Technologies")
web_frameworks = [
    "Angular", "AngularJS", "ASP.NET", "ASP.NET CORE", "Astro", "Blazor", "CodeIgniter", "Deno", "Django",
    "Drupal", "Elm", "Express", "FastAPI", "Fastify", "Flask", "Gatsby", "Htmx", "jQuery", "Laravel",
    "NestJS", "Next.js", "Node.js", "Nuxt.js", "Phoenix", "Play Framework", "React", "Remix",
    "Ruby on Rails", "Solid.js", "Spring Boot", "Strapi", "Svelte", "Symfony", "Vue.js", "WordPress", "Yii 2"
]

selected_frameworks = st.multiselect(
    "Which web frameworks and web technologies have you worked with?",
    web_frameworks
)

# Embedded Systems - Multi Select
st.header("Embedded Systems and Technologies")
embedded_systems = [
    "Arduino", "Boost.Test", "build2", "Catch2", "CMake", "Cargo", "cppunit", "CUTE", "doctest",
    "GNU GCC", "LLVM's Clang", "Meson", "Micronaut", "MSVC", "Ninja", "PlatformIO", "QMake",
    "Rasberry Pi", "SCons", "ZMK"
]

selected_embedded = st.multiselect(
    "Which embedded systems and technologies have you worked with?",
    embedded_systems
)

# Other Frameworks and Libraries - Multi Select
st.header("Other Frameworks and Libraries")
other_frameworks = [
    ".NET (5+)", ".NET Framework (1.0 - 4.8)", ".NET MAUI", "Apache Kafka", "Apache Spark", "Capacitor",
    "Cordova", "CUDA", "DirectX", "Electron", "Flutter", "GTK", "Hadoop", "Hugging Face Transformers",
    "Ionic", "JAX", "Keras", "Ktor", "MFC", "mlflow", "Numpy", "OpenCL", "Opencv", "OpenGL", "Pandas",
    "Qt", "Quarkus", "RabbitMQ", "React Native", "Roslyn", "Ruff", "Scikit-Learn", "Spring Framework",
    "SwiftUI", "Tauri", "TensorFlow", "Tidyverse", "Torch/PyTorch", "Xamarin"
]

selected_other_frameworks = st.multiselect(
    "Which other frameworks and libraries have you worked with?",
    other_frameworks
)

# Developer Tools - Multi Select
st.header("Developer Tools")
developer_tools = [
    "Ansible", "Ant", "APT", "Bun", "Chef", "Chocolatey", "Composer", "Dagger", "Docker", "Godot",
    "Google Test", "Gradle", "Homebrew", "Kubernetes", "Make", "Maven (build tool)", "MSBuild", "Ninja",
    "Nix", "npm", "NuGet", "Pacman", "Pip", "pnpm", "Podman", "Pulumi", "Puppet", "Terraform",
    "Unity 3D", "Unreal Engine", "Visual Studio Solution", "Vite", "Webpack", "Yarn"
]

selected_tools = st.multiselect(
    "Which developer tools for compiling, building and testing have you worked with?",
    developer_tools
)

# Submit Button
st.markdown("---")
if st.button("Submit Survey", type="primary"):
    # Collect all form data
    form_data = {
        "current_job": current_job,
        "education": education,
        "age": age,
        "employment_status": employment_status,
        "work_situation": work_situation,
        "programming_languages": selected_languages,
        "databases": selected_databases,
        "cloud_platforms": selected_cloud,
        "web_frameworks": selected_frameworks,
        "embedded_systems": selected_embedded,
        "other_frameworks": selected_other_frameworks,
        "developer_tools": selected_tools
    }
    
    # Display success message
    st.success("Survey submitted successfully! 🎉")
    
    # Display the collected data (for demonstration)
    with st.expander("View Submitted Data"):
        st.json(form_data)

# Add some styling
st.markdown("""
<style>
.stSelectbox > div > div {
    background-color: #f0f2f6;
}
.stMultiSelect > div > div {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)
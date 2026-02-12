"""
Quality Module Main Router
Routes to different quality module pages based on user selection
"""
import streamlit as st
from pages.quality import quality_create, quality_view, quality_dashboard

def render():
    """Main quality module router"""
    
    st.title("🎯 Trial Quality Matrix")
    
    # Check authentication
    is_authenticated = (
        st.session_state.get('username') is not None and 
        st.session_state.get('username') != ''
    )
    
    if not is_authenticated:
        st.warning("⚠️ Please login to access this page")
        return
    
    # Get user role
    role = st.session_state.get('role', 'user')
    
    # Navigation tabs based on role
    if role == 'manager':
        # ✅ MODIFIED: Manager only has Dashboard and View Records (no Create)
        tabs = st.tabs(["📊 Dashboard", "📋 View Records"])
        
        with tabs[0]:
            quality_dashboard.render()
        
        with tabs[1]:
            quality_view.render()
    
    else:  # user, admin, superuser
        tabs = st.tabs(["📝 Create Record", "📋 View My Records"])
        
        with tabs[0]:
            quality_create.render()
        
        with tabs[1]:
            quality_view.render()
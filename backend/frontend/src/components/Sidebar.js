import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import '../App.css';


const Sidebar = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const location = useLocation();

  const isActive = (path) => location.pathname === path;

  return (
    <aside className="sidebar">
      <div className="logo">
        <img src="/img/favicon.png" alt="Construction Pro Logo" />
        <h1>Construction Pro</h1>
      </div>
      <nav>
        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <rect x="3" y="3" width="7" height="7"></rect>
            <rect x="14" y="3" width="7" height="7"></rect>
            <rect x="14" y="14" width="7" height="7"></rect>
            <rect x="3" y="14" width="7" height="7"></rect>
          </svg>
          Dashboard
        </NavLink>
        <div className={`dropdown ${isDropdownOpen ? 'active' : ''}`}>
          <div 
            className={`nav-item ${isDropdownOpen ? 'active' : ''}`} 
            onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
            Masters
          </div>
          <div className="dropdown-content">
            <NavLink to="/masters/employee-type" className={({ isActive }) => isActive ? 'active' : ''}>Employee Type</NavLink>
            <NavLink to="/masters/vendor-type" className={({ isActive }) => isActive ? 'active' : ''}>Vendor Type</NavLink>
            <NavLink to="/masters/brand-type" className={({ isActive }) => isActive ? 'active' : ''}>Brand</NavLink>
            <NavLink to="/masters/employee-roles" className={({ isActive }) => isActive ? 'active' : ''}>Employee Role</NavLink>
            <NavLink to="/masters/item-list" className={({ isActive }) => isActive ? 'active' : ''}>Item List</NavLink>
          </div>
        </div>
        <NavLink to="/client" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
            <line x1="12" y1="22.08" x2="12" y2="12"></line>
          </svg>
          Client
        </NavLink>
      </nav>
    </aside>
  );
};

export default Sidebar;


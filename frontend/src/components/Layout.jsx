import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

function Layout() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Clear local storage and redirect to login
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header/Navigation */}
      <header className="bg-primary text-primary-foreground shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <Link to="/" className="text-2xl font-bold">WritingStuff</Link>
          <nav className="flex space-x-6 items-center">
            <Link to="/" className="hover:text-gray-200">Dashboard</Link>
            <Link to="/editor" className="hover:text-gray-200">Editor</Link>
            <button 
              onClick={handleLogout}
              className="bg-white/10 hover:bg-white/20 px-3 py-1 rounded-md"
            >
              Logout
            </button>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 container mx-auto px-4 py-6">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="bg-gray-100 py-4 text-center text-gray-600 text-sm">
        <div className="container mx-auto">
          <p>&copy; {new Date().getFullYear()} WritingStuff. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default Layout;

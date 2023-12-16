// src/components/Navbar.js

import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark">
      <span className="navbar-brand mb-0 h1" style={{ marginLeft: '10px' }}>CS162</span>
      <div>
        <Link to="/" style={{ color: 'white', marginRight: '10px' }}>Home</Link>
        <Link to="/add-task" style={{ color: 'white', marginRight: '10px' }}>Add Task</Link>
      </div>
    </nav>
  );
}

export default Navbar;

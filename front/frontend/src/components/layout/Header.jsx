function Header() {

  return (

    <header className="header">

      <div className="header-logo">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M4 4h16v11H7l-3 3V4z"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinejoin="round"
          />
        </svg>
      </div>

      <div className="header-content">
        <h1>AI Document Assistant</h1>
        <p>Upload a PDF and ask questions using AI</p>
      </div>

    </header>

  );

}

export default Header;

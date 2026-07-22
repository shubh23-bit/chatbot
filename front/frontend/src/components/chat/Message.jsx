function Message({

  role,

  text

}) {

  const isUser = role === "user";
  const isTyping = role === "assistant" && text === "";

  return (

    <div className={`message-row ${role}`}>

      <div className={`avatar ${role}`}>

        {isUser ? (
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M12 12a4 4 0 100-8 4 4 0 000 8zm-7 8a7 7 0 0114 0"
              stroke="currentColor"
              strokeWidth="1.8"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        ) : (
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="4" y="8" width="16" height="12" rx="2" stroke="currentColor" strokeWidth="1.8" />
            <path d="M12 8V4m-3 0h6" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
            <circle cx="9" cy="14" r="1.2" fill="currentColor" />
            <circle cx="15" cy="14" r="1.2" fill="currentColor" />
          </svg>
        )}

      </div>

      <div className={`bubble ${role}${isTyping ? " typing-indicator" : ""}`}>

        {isTyping ? (
          <>
            <span></span>
            <span></span>
            <span></span>
          </>
        ) : (
          text
        )}

      </div>

    </div>

  );

}

export default Message;

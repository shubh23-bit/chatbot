function Message({

  role,

  text

}) {

  return (

    <div className={`message ${role}`}>

      <div className="message-content">

        <strong>

          {

            role === "user"

              ? "👤 You"

              : "🤖 Assistant"

          }

        </strong>

        <p>{text}</p>

      </div>

    </div>

  );

}

export default Message;
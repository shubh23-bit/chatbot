function Message({ role, text }) {
  return (
    <div className={`message ${role}`}>
      <strong>
        {role === "user"
          ? "You"
          : "Bot"}
        :
      </strong>

      <p>{text}</p>
    </div>
  );
}

export default Message;
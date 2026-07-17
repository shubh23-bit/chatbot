import Message from "./Message";

function MessageList({

  messages

}) {

  return (

    <div className="message-list">

      {

        messages.map(

          (message, index) => (

            <Message

              key={index}

              role={message.role}

              text={message.text}

            />

          )

        )

      }

    </div>

  );

}

export default MessageList;
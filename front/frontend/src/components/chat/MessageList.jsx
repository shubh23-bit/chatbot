import { useEffect, useRef } from "react";
import Message from "./Message";

function MessageList({

  messages

}) {

  const bottomRef = useRef(null);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({ behavior: "smooth" });

  }, [messages]);

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

      <div ref={bottomRef} />

    </div>

  );

}

export default MessageList;

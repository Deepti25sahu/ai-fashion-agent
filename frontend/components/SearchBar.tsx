interface Props {

  message: string;

  setMessage: any;

  sendMessage: any;
}

export default function SearchBar({

  message,

  setMessage,

  sendMessage

}: Props) {

  return (

    <div className="
      bg-white
      p-4
      rounded-2xl
      shadow-xl
      flex
      gap-4
    ">

      <input

        type="text"

        value={message}

        onChange={(e) =>
          setMessage(e.target.value)
        }

        placeholder="
          Search luxury fashion...
        "

        className="
          flex-1
          p-4
          rounded-xl
          border
          outline-none
          text-black
        "
      />

      <button

        onClick={() => sendMessage()}

        className="
          bg-black
          text-white
          px-6
          rounded-xl
        "
      >
        Search
      </button>

    </div>
  );
}
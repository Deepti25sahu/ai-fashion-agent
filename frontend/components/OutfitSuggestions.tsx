interface Props {

  outfit: string[];

  sendMessage: any;
}

export default function OutfitSuggestions({

  outfit,

  sendMessage

}: Props) {

  if (outfit.length === 0)
    return null;

  return (

    <div className="
      px-10
      mt-10
    ">

      <h2 className="
        text-3xl
        font-bold
        mb-6
      ">
        Outfit Suggestions
      </h2>

      <div className="
        flex
        flex-wrap
        gap-4
      ">

        {outfit.map(
          (item, index) => (

            <button

              key={index}

              onClick={() =>
                sendMessage(item)
              }

              className="
                bg-black
                text-white
                px-5
                py-3
                rounded-full
                hover:scale-105
                transition
              "
            >
              {item}
            </button>
          )
        )}

      </div>

    </div>
  );
}

/** @type {import('./$types').PageLoad} */
 export async function load({url}) {
    let text = url.searchParams.get('t')

    const res = await fetch(`http://localhost:8080/search/line?text=${text}`);

    return {
      content: (await res.json()),
      text: text
    };
  }
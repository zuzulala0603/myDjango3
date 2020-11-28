console.log("인파이트")

const fetchPage = async (url) => {
  let headers = new Headers()
  headers.append("X-Requested-With", "XMLHttpRequest")
  return fetch(url, { headers })
}

const appendElements = async (scrollElement, counter, baseUrl) => {
  let url = `${baseUrl}?page=${counter + 1}`

  let req = await fetchPage(url);

  console.log(req)

  if (req.ok) {
    let body = await req.text();
    console.log(body)
    console.log(body.length)
    // Be careful of XSS if you do this. Make sure
    // you remove all possible sources of XSS.
    scrollElement.innerHTML += body;
  } else {
    end = true;
  }
}


const attachInfiniteScroll = (sentinel, scrollElement, baseUrl) => {

  //
  let counter = 1;
  let end = false;
  let observer = new IntersectionObserver(async (entries) => {
    let bottomEntry = entries[0];

    if (!end && bottomEntry.intersectionRatio > 0) {
      console.log("스크롤 이벤트!")
      await appendElements(scrollElement, counter, baseUrl);
      counter += 1;
    }
  })

  //


  observer.observe(sentinel);
}; 
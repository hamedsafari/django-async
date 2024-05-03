import {useEffect, useState} from "react";
import Axios from "axios";

export default function AsyncAPI() {
    const [text, setText] = useState()

    const readStream = async () => {
        Axios({
          url: "http://localhost:8080/async/chat/",
          method: "GET",
          responseType: "stream",
          onDownloadProgress: (progressEvent) => {
              setText(progressEvent.event.currentTarget.response);
          },
        })

    }
    useEffect(() => {
        console.log("Start")
        readStream();
    }, [])

    return (
        <main>
            <div>
                <p>Message: {text}</p>
            </div>
        </main>
    )
}
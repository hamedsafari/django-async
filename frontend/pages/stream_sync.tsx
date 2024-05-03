import {useEffect} from "react";
import axios from "axios";

export default function SyncAPI() {
    const readStream = async () => {
        const response = await axios.get("http://localhost:8080/async/chat/", {responseType: "stream"});
        const stream = response.data;
        stream.on("data", data => {
            data = data.toString();
            console.log(data);
        })
    }
    useEffect(() => {
        readStream();
    }, [])

    return (
        <main>
            <div>
                <p>Hello World!</p>
            </div>
        </main>
    )
}
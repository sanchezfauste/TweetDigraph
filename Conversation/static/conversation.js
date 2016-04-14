function changeSentiment(sentiment_select, comment) {
    var sentiment = document.getElementById(sentiment_select).value;
    if (sentiment == "negative") {
        document.getElementById(comment).className = "sentiment sentiment-negative";
    } else if (sentiment == "positive") {
        document.getElementById(comment).className = "sentiment sentiment-positive";
    } else {
        document.getElementById(comment).className = "sentiment sentiment-neutral";
    }
}

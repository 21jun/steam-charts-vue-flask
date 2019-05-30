export default function (raw) {
    var result = []
    result.push(['Name', 'playerCount', 'date'])
    raw.forEach(element => {
        // console.log(element)
        result.push([element[1], element[2], element[3]])
    });
    return result;
}
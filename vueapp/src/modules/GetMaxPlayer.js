export default function (raw) {
    var result = []
    result.push(['players', 'date'])
    raw.forEach(element => {
        result.push([element[1], element[0]])
        //result.push(element[0])
    });
    return result;
}
export default function (raw) {
    var result = []
    result.push(['players', 'date'])
    raw.forEach(element => {
        result.push([element[1], element[0]])
        //console.log(element[1])
    });
    return result;
}
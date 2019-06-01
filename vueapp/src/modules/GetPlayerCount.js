export default function (raw) {
    var result = []
    result.push(['name', 'max_player'])
    raw.forEach(element => {
        result.push([element[1], element[2]])
    });
    return result;
}
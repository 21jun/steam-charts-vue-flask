export default function (raw) {
    var result = []
    raw.forEach(element => {
        result.push([element[0], element[1], element[2]])
    });
    return result;
}
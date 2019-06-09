export default function (raw) {
    var result = []
    raw.forEach(element => {
        result.push([element[0], element[1], element[2], element[3], element[4], element[5]])
    });
    return result;
}
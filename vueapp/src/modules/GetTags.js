export default function (raw) {
    var result = []
    raw.forEach(element => {
        result.push(element[0])
    });
    return result;
}
export default function (raw) {
    
    var result = []
    result.push(['Name', 'appid'])
    raw.forEach(element => {
        // console.log(element)
        result.push([element[2], element[1]])
    });
    return result;
}
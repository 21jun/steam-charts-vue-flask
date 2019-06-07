export default function (raw) {
    
    var result = []
    // result.push(['Name', 'appid'])
    raw.forEach(element => {
        // console.log(element)
        result.push([element[1], element[0]])
    });
    return result;
}
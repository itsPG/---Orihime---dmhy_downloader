fs = require("fs");
PG = require("./html_tag.js");
parser_data = fs.readFileSync("./webtmp.txt", "utf-8");
try
{
	PG.parse(parser_data);
}
catch (err)
{
	console.log(err);
}


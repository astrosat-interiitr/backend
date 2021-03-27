from .models import *
head = """
<!doctype html>
<html>
  <head>
	<link href='https://fonts.googleapis.com/css?family=Allura' media="screen" rel='stylesheet'>
	<link href='https://fonts.googleapis.com/css?family=Monsieur La Doulaise' media="screen" rel='stylesheet'>
	<link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet' media="screen">
	<link href='https://fonts.googleapis.com/css?family=Tangerine' rel='stylesheet' media="screen">
	<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet' media="screen">
	<link rel="stylesheet" href="style.css" media="screen">
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" media="screen">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" media="screen">
	<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.selectboxit/3.8.0/jquery.selectBoxIt.css">

				  <!--meta tags-->
	<meta name="viewport" content="widtd=device-widtd, initial-scale=1.0">
	<meta name="description" content="tdis page is just a beginning of my project on collecting tde works for preservation of Madagascar Rainforests">
	<meta charset="UTF-8">
					<!-- scripts-->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.selectboxit/3.8.0/jquery.selectBoxIt.min.js"></script>
	<script src='https://kit.fontawesome.com/a076d05399.js'></script>
	<script src="script.js"> </script>
	<style>
		body{
			font-family: "Times New Roman" !important;
		}
/*-----------------------abhi ke liye sorf mani body----------------------------*/
h2{
	font-family: "Camberia Matd";
  font-size: 40px;
  font-weight: bold;

  text-align: center;
  margin-bottom: 50%;
}

p {
	font-size: 15px;
}

.paper{
	text-align: center !important;
}
.nw1{
	border-top: 2px solid black;
	border-radius: 5px;
}
.content{
	margin-left: 12%;
	text-align: "left";
	padding-top: 10px;
	padding-bottom: 10px;

	page-break-after: always;
}

td{
	text-align: left;
	text-decoration: italic;
	font-style: italic;
}
th{
	text-align: left;
}
 
.pp{
	text-align: left !important;
	margin-left: 10px;
	margin-bottom: 30px;
}


</style>
</head>
"""


publication_format = """
<p><b>Title:</b>{}</p>
<p><b>Authors:</b>{}</p>
<p><b>Keywords:</b>{}</p>
<p><b>Abstract:</b>{}</p>
"""

html = """
<body>
  <div class="paper">
	<h2 class="h2">{}</h2>
	
	<table class=content>
		<tr>
			<th> 
			Coordinates:</th>
			<td>
			RA(&#176 & deg min sec)
			</td>
			<td>
			DEC(&#176 & deg min sec)
			</td>
		</tr>
		<tr>
			<td>
			</td>
			<td>
				{}
			</td>
		 	<td>
				{}
			</td>
		</tr>
		<tr>
			<th>
				Galactic Coordinates:
			</th>
			<td>
				GLON&#176
			</td>
			<td>
				GLAT&#176
			</td>
		</tr>
		<tr>
			<td></td>
			<td>
				{}
			</td>
			<td>
				{}
			</td>
		</tr>
		<tr>
			<th>
				Searched by AstroSat:
			</th>
			<td>
				Yes
			</td>
		</tr>
		<tr>
			<th>
				Optical counterpart:
			</th>
			<td>
				{}
			</td>
		</tr>
	   	<tr>
	   		<th>
	   			Date of observations:
	   		</th>
	   		<td>
	   			{}
	   		</td>
	   	</tr>
	   	<tr>
	   		<th>
	   			Time of observations:
	   		</th>
	   		<td>
	   			{}
	   		</td>
	   	</tr>
	   	<tr>
	   		<th>
	   			Observations Ids
	   		</th>
	   		<td>
			 {}
	   		</td>
	   	</tr>
	   	<tr>
	   		<th>
	   			Telescopes used to observe:
	   		</th>
	   		<td>
	   			{}
	   		</td>
	   	</tr>

			<hr class=nw1>
	</table>
	{}
</div>
</body>
</html>"""

publication_block = """
<div class="pp">
		<h2>Papers Published</h2>
		{} </div>
"""


def generateHTML(publication_ids, cosmic_source_id, astrosat_ids):
	print(cosmic_source_id)


	publications = ""
	if len(publication_ids) > 0:
		for publication in publication_ids:
			currentPublication = Publication.objects.get(id = publication)
			publication_data = publication_format.format(
				currentPublication.title,
				currentPublication.authors,
				currentPublication.keyword,
				currentPublication.abstract,
			)
			publications = publications + publication_data + "<br /><br /><br />"
		publications = publication_block.format(publications)

	date_of_observation = ""
	time_of_observation = ""
	obervation_ids = ""
	telescope_used = ""

	if len(astrosat_ids) > 0:
		for astrosat in astrosat_ids:
			currentAstrosat = Astrosat.objects.get(id = astrosat)
			date_of_observation = date_of_observation + currentAstrosat.date + ", "
			time_of_observation = time_of_observation + currentAstrosat.time + ", "
			telescope_used = telescope_used + currentAstrosat.telescope + ", "
			obervation_ids = obervation_ids + currentAstrosat.observation_id + ", "

	cosmic = CosmicSource.objects.get(id= cosmic_source_id)
	htmlToReturn = html.format(
		cosmic.name,
		cosmic.equatorial_ra,
		cosmic.equatorial_dec,
		cosmic.galactic_longitude,
		cosmic.galactic_latitude,
		cosmic.optical_counterpart_name,
		date_of_observation, 
		time_of_observation,
		obervation_ids,
		telescope_used,
		publications
	)


	htmlToReturn = head + htmlToReturn
	return htmlToReturn

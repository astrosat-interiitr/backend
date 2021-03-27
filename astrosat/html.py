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
    margin: 20vh 40vh 0vh 40vh;
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
    <hr class="nw1">
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
    			74.458&#176
    		</td>
    	 	<td>
    			35.343&#176
    		</td>
    	</tr>
    	<tr>
    		<td></td>
    		<td>
    			16&#176 57' 49.8''
    		</td>
    		<td>
    			+35&#176 20' 33''
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
    			58.2
    		</td>
    		<td>
    			+37.5
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
    			Position derived from obs:
    		</th>
    		<td>
    			Optical
    		</td>
    	</tr>
    	<tr>
    		<th>
    			Type of the source:
    		</th>
    		<td>
    			X--Ray Binary
    		</td>
    	</tr>
    	<tr>
    		<th>
    			Optical counterpart:
    		</th>
    		<td>
    			HZ Her
    		</td>
    	</tr>
    	<tr>
    		<th>
    			Distance to the source center:
    		</th>
    		<td>0.52 arcsec</td>
       	</tr>
       	<tr>
       		<th>
       			Date of observations:
       		</th>
       		<td>
       			2018/09/17, 2018/19/21, 2020/02/20
       		</td>
       	</tr>
       	<tr>
       		<th>
       			Time of observations:
       		</th>
       		<td>
       			8:09:52, 
       		</td>
       	</tr>
       	<tr>
       		<th>
       			Observations Ids
       		</th>
       		<td>
             first id, second id, third id 	
       		</td>
       	</tr>
       	<tr>
       		<th>
       			Telescopes used to observe:
       		</th>
       		<td>
       			laxpc1, laxpc2, laxpc3...
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
    	<h2>Paper Published</h2>
        {} </div>
"""
def generateHTML(data):

    print(data)

    
    publications = ""

    if "publication_ids" in data.keys():
        for publication in data['publication_ids']:
            currentPublication = Publication.objects.get(id = publication)
            publication_data = publication_format.format(
                currentPublication.title,
                currentPublication.authors,
                currentPublication.keyword,
                currentPublication.abstract,
            )
            publications = publications + publication_data
        publications = publication_block.format(publications)


    
    htmlToReturn = html.format("Her X-1; 1656+354", publications)
    htmlToReturn = head + htmlToReturn
    return htmlToReturn

# Insert_Fetch
Insert papers and conferences data into data base and fetch results based on keywords


## Papers collection structure

- title: < Title of the paper >
- authors: < List of authors >
- venue: < Conference name >
- year: < Organised year of conference >
- url: < URL of the paper >
- rank: < Rank of the paper, NA if not found >
- keyword: < Keywords to search >

### Example paper:
```sh 
{
	"_id" : ObjectId("617ff6d8ab766c83e23d5977"),
	"title" : "Lifelong Machine Learning Systems - Beyond Learning Algorithms.",
	"authors" : [
 		"Daniel L. Silver",
 		"Qiang Yang 0001",
 		"Lianghao Li"
	],
	"venue" : "AAAI Spring Symposium - Lifelong Machine Learning",
	"year" : "2013",
	"url" : "https://dblp.org/rec/conf/aaaiss/SilverYL13",
	"rank" : "A",
	"keywords" : [
 		"machine learning",
 		"computer vision"
	]
}
 ```
### Indexes Created:
-   On title,year: To check for duplicates and update keyword before inserting
-   On keywords: To fetch data related to keyword from database

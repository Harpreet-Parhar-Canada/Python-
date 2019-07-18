
console.log("Hello from the functions.js v2");

	function myFunction(xx, yy){
			console.log("Hello from myFunction v2",xx, yy);
						const value=xx+ "-" +yy;
						return value;
}
						
const value1=myFunction("Rocks","Rings");
const value2=myFunction("Coding","Fun");

console.log("v1:",value1);
console.log("v2:",value2);

const func=myFunction;

console.log(func("Hello","World"));	
const getanswer=my_add(3,2,3);

console.log("console_result",getanswer);
console.log("console_result",my_add(2,22,222));

const callingstrfunction=my_email("harpree","parhar");
console.log("console_callingbyvariable:",callingstrfunction);
console.log("console_result",my_email("jones","smith"));

function my_add(a,b,c)
{
	const x=parseInt(a);
	const y=parseInt(b);
	const z=parseInt(c);
	const add1=a+b+c;
	return add1;
	//console.log("Result",add1);
}	


function my_email(str1,str2)
{
const  strcopy=str1;
const str2copy=str2;
const stremail="evolveu.ca";
const addingstr=str1+"."+ str2+"@"+stremail;
return addingstr;



}				

console.log("array function",array_func(4));

function array_func(number1)
{
var arrayname=[5,10,15,20];
arrayname.length=number1;
var i;
var sum=0;
if(number1<5)
{ 

for (i=0;i<arrayname.length;i++)
 { 
 	sum=sum+arrayname[i];
 	console.log(arrayname[i] +" i="+ i);
}
return sum;
}

else
{console.log("Array's number lenght is limited");}


}

const arryName=["this is string","that is also string","what about this","what about that this"];
		 
const serach1="this"; 
const serach2="is"; 

console.log(searchoperation(arryName,serach1));
function searchoperation(arrayName1,message){
 for( var i=0;i<arrayName1.length;i++) {
 	
 	str = arrayName1[i];
 	position = str.search(message);
       if( position > -1)
		{console.log("we found",i);}
 	else{
 		console.log(" not found");
 	}
 }

}
		 

					






			





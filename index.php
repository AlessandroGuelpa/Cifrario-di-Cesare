<html> 
<body> 
<form action = "index.php" method = "POST">
    <input type = "text" name = "msg" placeholder="Messaggio">
    <input type = "text" name = "key" placeholder="Chiave">
    <input type = "submit" value="Cifra!">
</form>
<?php 
function crypted($m, $k){
    for($i = 0; $i < strlen($m);$i++){
        $c .= chr((ord($m[$i])+$k)%255);
    }
    return $c;
}
if(isset($_POST['msg']) && isset($_POST['key'])){
$msg = $_POST['msg'];
$key = $_POST['key'];
$msg_c = crypted($msg, $key);
echo "Messaggio in chiaro:$msg <br>";
echo "Messaggio cifrato:$msg_c <br>";
}
?>
</body> 
</html>

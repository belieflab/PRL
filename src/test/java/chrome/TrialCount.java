package chrome;		

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;		
import org.testng.annotations.Test;		

public class TrialCount {		
		@Test
	   public void reliability() throws InterruptedException {
		   
		   String os = System.getProperty("os.name").toLowerCase();
		   
		   //System.setProperty("webdriver.chrome.driver", /usr/bin/chromedriver);
				  
		   WebDriver driver = new ChromeDriver();
		   
		   // Open driver , navigate to google.com
		   driver.get("https://google.com");
		   String getTitle = driver.getTitle();
		   Assert.assertEquals(getTitle, "Google");
		   
		   driver.getCurrentUrl();
		   
		   // Navigate to the required web application
		   driver.get("https://belieflab.yale.edu/capr/prl/code/card_task_01.php");

		   // Enter test ID
		   driver.switchTo().alert().sendKeys("jenkinsTestChrome");
			driver.switchTo().alert().accept();

			// Confirm test ID
			driver.switchTo().alert().accept();
		   
		   // Assertion test for TrialCount
		   JavascriptExecutor js = (JavascriptExecutor) driver;
		   Long ActualTrialCount = (long) 40;
		   Long ExpectedTrialCount = (Long) js.executeScript("return trialsPerBlock");
		   Assert.assertEquals(ExpectedTrialCount, ActualTrialCount);
		   
		   

		   //Close Driver
		   driver.quit();
		}		
}	
import java.io.*;
import java.util.regex.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;



public class TweetContentClassification2 {

	public static void main(String[] args) throws Exception {
		
		File in = new File("hh.json");
		File rel = new File("hh-relevant-v0.json");
		File irr = new File("hh-irrelevant-v0.json");
		String subtopic = "hh";
		
		readWriteFile(in, rel, irr, subtopic);
		
		in = new File("se.json");
		rel = new File("se-relevant-v0.json");
		irr = new File("se-irrelevant-v0.json");
		subtopic = "se";
		
		readWriteFile(in, rel, irr, subtopic);
		
		in = new File("ob.json");
		rel = new File("ob-relevant-v0.json");
		irr = new File("ob-irrelevant-v0.json");
		subtopic = "ob";
		
		readWriteFile(in, rel, irr, subtopic);
		
		in = new File("nv.json");
		rel = new File("nv-relevant-v0.json");
		irr = new File("nv-irrelevant-v0.json");
		subtopic = "nv";
		
		readWriteFile(in, rel, irr, subtopic);
	}
	
	public static void readWriteFile(File in, File outREL, File outIRR, String subtopic) throws Exception {
		try {
			BufferedReader inputStream = new BufferedReader(new FileReader(in));
			BufferedWriter outputRELStream = new BufferedWriter(new FileWriter(outREL));
			BufferedWriter outputIRRStream = new BufferedWriter(new FileWriter(outIRR));
			
			String inLine = null;
			List<String> tweets = new ArrayList<String>();
			
			while ((inLine = inputStream.readLine()) != null) {
				String tweetContent = getTweet(inLine);
				tweets.add(tweetContent);
				
				if(isRelevantTweet(tweetContent, subtopic) && !isJoke(tweetContent))
					outputRELStream.write(inLine + "\n");
				else
					outputIRRStream.write(inLine + "\n");
			}
			
			inputStream.close();
			outputRELStream.close();
			outputIRRStream.close();
			
			//topNGram(1,tweets, new File("1gram-"+subtopic+".txt"));
			//topNGram(2,tweets, new File("2gram-"+subtopic+".txt"));
			//topNGram(3,tweets, new File("3gram-"+subtopic+".txt"));
			
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
		catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	private static String getTweet(String text) {
		String tweet = text;
		Pattern p = Pattern.compile("\"text\":\\s+\".+\",");
		Matcher m = p.matcher(text.toLowerCase());
		while(m.find()) {
			tweet = m.group(0);
		}
		tweet = tweet.substring(5,tweet.length()-2);
		System.out.println(tweet);
		return tweet;
	}
	
	
	private static boolean isJoke(String text) {
		boolean isAJoke = false;
		if(isVickynisasi(text))
			isAJoke = true;
		else {
			Pattern pa = Pattern.compile("(ha)+h?[^a-z]+");
			Matcher ma = pa.matcher(text.toLowerCase());	
			int countLOL = 0;
			while(ma.find()) {
				if(!ma.group(0).equals(text.toLowerCase())) {
					countLOL++;
				}
			}
			if(countLOL > 1 || Pattern.matches("(wk)+w?\\s+", text.toLowerCase())) {
				isAJoke = true;
			}
		}
		return isAJoke;
	}
	
	
	private static boolean isVickynisasi(String text) {
		boolean vickynisasi = false;
		
		Pattern p = Pattern.compile("isasi[^a-z]+");
		Matcher m = p.matcher(text.toLowerCase());	
		int countIsasi = 0;
		while(m.find()) {
			if(!m.group(0).equals(text)) {
				countIsasi++;
			}
		}
		p = Pattern.compile("imunisasi[^a-z]+");
		m = p.matcher(text.toLowerCase());	
		int countImunisasi = 0;
		while(m.find()) {
			if(!m.group(0).equals(text)) {
				countImunisasi++;
			}
		}
		
		if((countIsasi > 1 && countIsasi - countImunisasi > 0) || text.toLowerCase().contains("kudeta") || text.toLowerCase().contains("konspirasi") || text.toLowerCase().contains("kontroversi") || text.toLowerCase().contains("vicky"))
			vickynisasi = true;
		
		return vickynisasi;
	}
	
	
	private static boolean isRelevantTweet(String text, String subtopic) {
		boolean isRelevant = true;
      if (subtopic=="hh") {
         isRelevant = halalHaramRelevantTweetCheck(text);
      } else if (subtopic=="nv") {
      
         isRelevant = newVaccineRelevantTweetCheck(text);
      } else if (subtopic=="se") {
         isRelevant = sideEffectRelevantTweetCheck(text);
      } else if (subtopic=="ob") {
         isRelevant = outbreakRelevantTweetCheck(text);
      }
      /*
		switch(subtopic) {
			case "hh":
				isRelevant = halalHaramRelevantTweetCheck(text);
				break;
			case "nv":
				isRelevant = newVaccineRelevantTweetCheck(text);
				break;
			case "se":
				isRelevant = sideEffectRelevantTweetCheck(text);
				break;
			case "ob":
				isRelevant = outbreakRelevantTweetCheck(text);
				break;
			default:
				break;
		}*/
		return isRelevant;
	}
	
	
	private static boolean sideEffectRelevantTweetCheck(String text) {
		boolean bool = true;
		
		if(text.toLowerCase().contains("nyeri sendi") || text.toLowerCase().contains("laktosa") || text.toLowerCase().contains("kanker") || text.toLowerCase().contains("korupsi") || text.toLowerCase().contains("batuk") || text.toLowerCase().contains("pilek") || text.toLowerCase().contains("hati ") || text.toLowerCase().contains(" hati") || text.toLowerCase().contains("cinta") || text.toLowerCase().contains("pacar") || text.toLowerCase().contains("jomblo") || text.toLowerCase().contains("beling") || text.toLowerCase().contains("olahraga") || text.toLowerCase().contains("rumah sakit") || text.toLowerCase().contains("demam berdarah") || text.toLowerCase().contains("rabies") || text.toLowerCase().contains("hewan") || text.toLowerCase().contains("binatang") || text.toLowerCase().contains("sapi") || text.toLowerCase().contains("kucing") || text.toLowerCase().contains("anjing") || text.toLowerCase().contains("nyamuk") || text.toLowerCase().contains("india") || text.toLowerCase().contains("brasil") || text.toLowerCase().contains("perancis") || text.toLowerCase().contains("texas")) {
			bool = false;
		}
					
		else if(!(text.toLowerCase().contains("menyebabkan") || text.toLowerCase().contains("akibat")) && (text.toLowerCase().contains("influenza") || text.toLowerCase().contains("alergi"))) {
			bool = false;
		}
		
		else if(!text.toLowerCase().contains("imunisasi") && text.toLowerCase().contains("imun")) {
			if(text.toLowerCase().contains("sistem") || text.toLowerCase().contains("sstem") || text.toLowerCase().contains("tubuh") ||  text.toLowerCase().contains("daya") ) {
				bool = false;
			}
			else if(!(text.toLowerCase().contains("abis imun") || text.toLowerCase().contains("hbs imun") || text.toLowerCase().contains("abs imun") ||  text.toLowerCase().contains("di imun") || text.toLowerCase().contains("bayi") || text.toLowerCase().contains("baby") || text.toLowerCase().contains("anak") || text.toLowerCase().contains(" nak ") || text.toLowerCase().contains(" nak.") || text.toLowerCase().contains("campak") || text.toLowerCase().contains("polio") || text.toLowerCase().contains("dpt") || text.toLowerCase().contains("dtp")  || text.toLowerCase().contains("mmr") || text.toLowerCase().contains("hib") || text.toLowerCase().contains("bcg"))) {
				bool = false;
			}				
		}
		return bool;
 	}
	
	
	private static boolean outbreakRelevantTweetCheck(String text) {
		boolean bool = true;
		
		if(text.toLowerCase().contains("israel") || text.toLowerCase().contains("nigeria") || text.toLowerCase().contains("brazil") || text.toLowerCase().contains("texas") || text.toLowerCase().contains("suriah") || text.toLowerCase().contains("sudan") || text.toLowerCase().contains("pakistan") || text.toLowerCase().contains("taliban") || text.toLowerCase().contains("pbb") || text.toLowerCase().contains("amerika") || text.toLowerCase().contains("lumba-lumba") || text.toLowerCase().contains("kertas") || text.toLowerCase().contains("campakkan") || text.toLowerCase().contains("campakin") || text.toLowerCase().contains("campak kan") || text.toLowerCase().contains("campakan") || text.toLowerCase().contains("pacar")) {
			bool = false;
		}
		
		return bool;
 	}

	
	private static boolean halalHaramRelevantTweetCheck(String text) {
		boolean bool = true;		
					
		if(text.toLowerCase().contains("flu babi") || text.toLowerCase().contains("flu burung") || text.toLowerCase().contains("skotlandia") || text.toLowerCase().contains("glasgow")) {
			bool = false;
		}
		
		return bool;
 	}	
	
	
	
	private static boolean newVaccineRelevantTweetCheck(String text) {
		boolean bool = false;
		
		if(text.toLowerCase().contains("pentavalen") || text.toLowerCase().contains("pentabio") || text.toLowerCase().contains("ventafalen") || text.toLowerCase().contains("venta bio") || text.toLowerCase().contains("5 in 1")) {
			bool = true;
		}
		else if(text.toLowerCase().contains("vaksin baru") && (text.toLowerCase().contains("anak") || text.toLowerCase().contains("balita") || text.toLowerCase().contains("menkes"))) {
			bool = true;
		}
		
		return bool;
 	}
	
	
	private static void topNGram(int n, List<String> tweetContents, File nGramDoc) throws Exception {
		
		Map<String,Integer> mpNGram = new HashMap<String,Integer>();
		for(int y=0; y<tweetContents.size(); y++) {
			String text = (String)tweetContents.get(y);
			String[] tokens = text.split("\\s+");
			for(int z=0; z<tokens.length-n+1; z++) {
				String nGram = tokens[z];
				if(n > 1) {
					for(int m=1; m<n; m++) {
						nGram = nGram + " " + tokens[z+m];
					}
				}
				nGram = nGram.toLowerCase();
				if(mpNGram.containsKey(nGram)) {
					Integer freq = mpNGram.get(nGram);
					mpNGram.put(nGram, freq+1);
				}
				else {
					mpNGram.put(nGram, 1);
				}
			}
		}
	
		int[] vals = new int[mpNGram.size()];
		String[] strs = new String[mpNGram.size()];
		int id = 0;
		Iterator it = mpNGram.entrySet().iterator();
		while(it.hasNext()) {
			Map.Entry pairs = (Map.Entry)it.next();
         //vals[id] = pairs.getValue();
			vals[id] = (Integer)pairs.getValue();
			strs[id] = (String)pairs.getKey();
			id++;
			it.remove(); // avoids a ConcurrentModificationException
		}
		// sorting
		for(int f=0; f<vals.length; f++) {
			for(int g=f+1; g<vals.length; g++) {
				if(vals[f] < vals[g]) {
					int tmpVal = vals[f];
					vals[f] = vals[g];
					vals[g] = tmpVal;
					String tmpStr = strs[f];
					strs[f] = strs[g];
					strs[g] = tmpStr;
				}
			}
		}
		
		try {
			BufferedWriter outputStream = new BufferedWriter(new FileWriter(nGramDoc));
			//print Hash Map	
			for(int h=0; h<vals.length; h++) {
				outputStream.write("\"" + strs[h] + "\", " + vals[h] + "\n");
				//System.out.println("\"" + strs[h] + "\", " + vals[h]);  
			}
			outputStream.close();
		} 
		catch (IOException e) {
			e.printStackTrace();
		}
 	}
	
}

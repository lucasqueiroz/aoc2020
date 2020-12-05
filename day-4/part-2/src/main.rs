use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use regex::Regex;

fn main() -> io::Result<()> {
    let file = File::open("src/input")?;
    let reader = BufReader::new(file);

    let mut current: String = "".to_string();
    let mut valid = 0;

    for line in reader.lines() {
        let line_str: String = line?;
        if !(line_str.eq("")) {
            current.push_str(&line_str);
        } else {
            if
                current.contains("byr:") &&
                current.contains("iyr:") &&
                current.contains("eyr:") &&
                current.contains("hgt:") &&
                current.contains("hcl:") &&
                current.contains("ecl:") &&
                current.contains("pid:")
            {
                let bcurrent = &current.clone();

                let mut re = Regex::new(r"byr:(\d{4})").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let byr = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"iyr:(\d{4})").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let iyr = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"eyr:(\d{4})").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let eyr = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"hgt:(\d{2,3}[ic][nm])").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let hgt = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"hcl:(#[0-9a-f]{6})").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let hcl = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"ecl:(gry|amb|blu|brn|grn|hzl|oth)").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let ecl = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                re = Regex::new(r"pid:(\d{9})").unwrap();
                if !re.is_match(bcurrent) {
                    continue;
                }
                let pid = re.captures(bcurrent).unwrap().get(1).unwrap().as_str();

                current = "".to_string();

                if
                    byr.is_empty() ||
                    iyr.is_empty() ||
                    eyr.is_empty() ||
                    hgt.is_empty() ||
                    hcl.is_empty() ||
                    ecl.is_empty() ||
                    pid.is_empty()
                {
                    continue;
                }

                let byr_val: u32 = byr.parse().expect("wanted a number");

                if byr_val < 1920 || byr_val > 2020 {
                    continue;
                }

                let iyr_val: u32 = iyr.parse().expect("wanted a number");

                if iyr_val < 2010 || iyr_val > 2020 {
                    continue;
                }

                let eyr_val: u32 = eyr.parse().expect("wanted a number");

                if eyr_val < 2020 || eyr_val > 2030 {
                    continue;
                }

                if hgt.contains("cm") {
                    let hgt_val: u32 = hgt.replace("cm", "").parse().expect("wanted a number");

                    if hgt_val < 150 || hgt_val > 193 {
                        continue;
                    }
                } else {
                    let hgt_val: u32 = hgt.replace("in", "").parse().expect("wanted a number");

                    if hgt_val < 59 || hgt_val > 76 {
                        continue;
                    }
                }

                valid = valid + 1;
            }
            current = "".to_string();
        }
    }
    println!("{}", valid);

    Ok(())
}

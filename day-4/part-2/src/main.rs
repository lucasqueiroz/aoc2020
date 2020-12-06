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
            let bcurrent = &current.clone();
            current = "".to_string();

            let mut re = Regex::new(r"byr:(?:200[0-2]|19[2-9][0-9])").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"iyr:20(?:1[0-9]|20)").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"eyr:20(?:2[0-9]|30)").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"hgt:(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"hcl:#[0-9a-f]{6}[\D^a-f\n]?").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"ecl:(?:amb|blu|brn|gry|grn|hzl|oth)[\D\n]?").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            re = Regex::new(r"pid:(?:\d{9})(?:$|\n|\D|[bieh])").unwrap();
            if !re.is_match(bcurrent) {
                continue;
            }

            valid = valid + 1;
        }
    }
    println!("{}", valid);

    Ok(())
}

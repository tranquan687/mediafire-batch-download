
import mediafire_dl
import argparse
import os 
def main():
    desc = 'Simple command-line script to download files from mediafire'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url')
    # parser.add_argument('-o', '--output', help='output filename',default=None)
    parser.add_argument('--out_folder', help='output filename',default='./output')
    

    args = parser.parse_args()
    
    if not os.path.exists(args.out_folder): 
	
	# if the demo_folder directory is not present 
	# then create it. 
        os.makedirs(args.out_folder)
    new_wd = os.path.abspath(args.out_folder) 
    cwd = os.chdir(new_wd)
    
    
    link = args.url.split('/')[-2]
    lst_keys = link.split(',')
    
    for key in lst_keys:
        url = "https://mediafire.com/?"+ key
        mediafire_dl.download(url, quiet=False)
        
if __name__ == "__main__":
    main()

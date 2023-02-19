import mkdocs_gen_files
import glob
import frontmatter

from datetime import datetime
from itertools import groupby

from mkdocs_git_revision_date_localized_plugin.util import Util
from babel.dates import get_timezone
from dateutil import tz

with mkdocs_gen_files.open("docs.md", "w") as f:
    print("### 모든 문서 들\n", file=f)

    util = Util()
    docs = []

    KST = tz.gettz('Asia/Seoul')
    for filename in glob.iglob("docs/" + '**/**.md', recursive=True):
        if(not filename.endswith("excalidraw.md") and not filename.startswith("docs/til/til")) :
            createdAtTimestamp = util.get_git_commit_timestamp(filename, True) 
            updateAtTimestamp = util.get_git_commit_timestamp(filename)

            createdAtKst = datetime.fromtimestamp(createdAtTimestamp, KST)
            updateAtKst = datetime.fromtimestamp(updateAtTimestamp, KST)

            docs.append((filename, createdAtTimestamp, updateAtTimestamp, createdAtKst, updateAtKst))
    
    docs.sort(key = lambda x: -x[1])
    docsWithYearMonth = groupby(docs, lambda x: (x[3].date().year, x[3].date().month))

    for yearMonth, docs in docsWithYearMonth:
        print(f'### {yearMonth[0]} 년 {yearMonth[1]} 월', file = f)

        for doc in docs:


            ## 작성 일
            createdAtDate = doc[3].date().strftime("%Y-%m-%d")

            ## 문서 경로
            docPath = doc[0][:-3]
            docPath = docPath[5:]
            if docPath.endswith("/index") :
                docPath = docPath[:-5]
            docPath = "Haha-Blog/../../" + docPath

            try :
                yaml = frontmatter.load(doc[0])
            except :
                yaml = {"title" : docPath}

            ## tags
            docTags = yaml.get('tags')
            if(docTags is None) :
                docTags = []

            docTagConcat = ""
            for tag in docTags :
                docTagConcat = docTagConcat + "<code>" + tag + "</code>" +" "

            ## 문서 제목
            docTitle = yaml.get('title')
            if(docTitle is None) :
                docTitle = docPath
            
            
            print(f'{createdAtDate} {docTagConcat} [{docTitle}]({docPath}) \n', file= f)
from upload_machine.utils.uploader.piggo_upload import piggo_upload
from upload_machine.utils.uploader.hdsky_upload import hdsky_upload
from upload_machine.utils.uploader.audience_upload import audience_upload
from upload_machine.utils.uploader.ssd_upload import ssd_upload
from upload_machine.utils.uploader.pter_upload import pter_upload
from upload_machine.utils.uploader.hhclub_upload import hhclub_upload
from upload_machine.utils.uploader.lemonhd_upload import lemonhd_upload
from upload_machine.utils.uploader.hdpt_upload import hdpt_upload
from upload_machine.utils.uploader.wintersakura_upload import wintersakura_upload
from upload_machine.utils.uploader.carpt_upload import carpt_upload
from upload_machine.utils.uploader.hdfans_upload import hdfans_upload
from upload_machine.utils.uploader.hare_upload import hare_upload





def auto_upload(siteitem,file,record_path,qbinfo,basic,hashlist):
    return eval(siteitem.sitename+'_upload(siteitem,file,record_path,qbinfo,basic,hashlist)')
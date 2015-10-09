class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == "" or version2 == "":
            return 0;



        idx = 0;
        list_v1 = version1.split('.');
        list_v2 = version2.split('.');

        while 1:
            if idx == len(list_v1) or idx == len(list_v2):
                break;
            # print int(list_v1[idx])
            # print int(list_v2[idx])
            if int(list_v1[idx]) > int(list_v2[idx]):
                return 1;
            elif int(list_v1[idx]) < int(list_v2[idx]):
                return -1;

            idx += 1;

        if idx == len(list_v1) and idx < len(list_v2):
            if int(list_v2[idx]) == 0:
                return 0;
            return -1;

        if idx < len(list_v1) and idx == len(list_v2):
            if int(list_v1[idx]) == 0:
                return 0;
            return 1;

        return 0;
